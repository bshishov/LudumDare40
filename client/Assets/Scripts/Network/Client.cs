using System;
using System.Collections.Generic;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using Assets.Scripts.Utils;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace Assets.Scripts.Network
{
    public class Client : Singleton<Client>
    {
        public delegate void Messagehandler(Message message);

        public bool IsActive
        {
            get { return _tcpClient != null && _tcpClient.Connected && _tcpStream != null; }
        }

        public bool IsInGame { get; private set; }
        public bool IsInQueue { get; private set; }
        public string GameId { get; private set; }
        public string Side { get; private set; }
        
        public string Host = "127.0.0.1";
        public int Port = 8976;
        public string SceneToLoad = "Battle";

        public event Messagehandler MessageReceived;
        public event Messagehandler GameMessageReceived;
        public event Messagehandler LobbyMessageReceived;

        private TcpClient _tcpClient;
        private NetworkStream _tcpStream;
        private Thread _listenThread;
        private readonly byte[] _readBuffer = new byte[8192];
        private readonly Dictionary<string, List<Messagehandler>> _messageSubscribers = 
            new Dictionary<string, List<Messagehandler>>(); 

        // Dispatching
        private readonly List<System.Action> _dispatchList = new List<Action>();
        private readonly List<System.Action> _dispatchListCopy = new List<Action>();
        private bool _dispatching = false;
        private readonly System.Object _dispatchLock = new System.Object();


        void Awake()
        {
            DontDestroyOnLoad(gameObject);
        }

        void Start ()
        {
		    _tcpClient = new TcpClient();
            _tcpClient.BeginConnect(Host, Port, new AsyncCallback(OnConnect), _tcpClient);

            MessageReceived += OnMessageReceive;

            Subscribe(Protocol.MsgSrvHello, message =>
            {
                Debug.LogFormat("Hello: {0}", message);
            });

            Subscribe(Protocol.MsgSrvGameBegin, message =>
            {
                Side = message.Body[Protocol.KeySide];
                Debug.LogFormat("Game begin");
            });

            Subscribe(Protocol.MsgSrvQueueStarted, message =>
            {
                IsInQueue = true;
                Debug.Log("Queue started");
            });

            Subscribe(Protocol.MsgSrvQueueStopped, message =>
            {
                IsInQueue = false;
                Debug.Log("Queue stopped");
            });

            Subscribe(Protocol.MsgSrvQueueGameCreated, message =>
            {
                IsInQueue = false;
                IsInGame = true;
                GameId = message.Body[Protocol.KeyGameId];
                Debug.LogFormat("Game started, id: {0}", GameId);
                SceneManager.LoadScene(SceneToLoad);
            });
        }

        private void OnMessageReceive(Message message)
        {
            // Message domain dispatching
            if (message.DomainIs(Protocol.MsgDomainLobby))
            {
                if(LobbyMessageReceived != null)
                    LobbyMessageReceived.Invoke(message);
            }
            else if (message.DomainIs(Protocol.MsgDomainGame))
            {
                if (GameMessageReceived != null)
                    GameMessageReceived.Invoke(message);
            }

            if (_messageSubscribers.ContainsKey(message.Head))
            {
                var subs = _messageSubscribers[message.Head];
                if (subs != null)
                {
                    foreach (var messagehandler in subs)
                    {
                        messagehandler.Invoke(message);
                    }
                }
            }
        }

        public void Subscribe(string head, Messagehandler handler)
        {
            if (_messageSubscribers.ContainsKey(head))
            {
                var subs = _messageSubscribers[head];
                if (subs == null)
                    _messageSubscribers[head] = new List<Messagehandler> { handler };
                else
                    _messageSubscribers[head].Add(handler);
            }
            else
            {
                _messageSubscribers.Add(head, new List<Messagehandler>{ handler });
            }
        }

        public void UnSubscribe(string head, Messagehandler handler)
        {
            if(!_messageSubscribers.ContainsKey(head))
                return;

            var subs = _messageSubscribers[head];

            if (subs == null || !subs.Contains(handler))
                return;

            subs.Remove(handler);
        }

        private void Listen()
        {
            while (true)
            {
                if (_tcpClient != null && !_tcpClient.Connected) return;
                
                try
                {
                    var bytesReceived = _tcpStream.Read(_readBuffer, 0, _readBuffer.Length);
                    var messageRaw = Encoding.UTF8.GetString(_readBuffer, 0, bytesReceived);
                    var msg = new Message(messageRaw);
                    if(MessageReceived != null)
                        Dispatch(() => MessageReceived.Invoke(msg));
                }
                catch (SocketException ex)
                {
                    Debug.LogWarningFormat("Error while receiving a message: {0}", ex);
                    return;
                }
                
            }
        }

        public void Send(string message)
        {
            if (_tcpClient != null && _tcpClient.Connected && _tcpStream != null)
            {
                var msgBuff = Encoding.UTF8.GetBytes(message);

                var buff = new byte[msgBuff.Length + Protocol.MessageSeparator.Length];
                System.Buffer.BlockCopy(msgBuff, 0, buff, 0, msgBuff.Length);
                System.Buffer.BlockCopy(Protocol.MessageSeparator, 0, buff, msgBuff.Length, Protocol.MessageSeparator.Length);
                
                _tcpStream.BeginWrite(buff, 0, buff.Length, OnSend, _tcpClient);
                Debug.LogFormat("Sending: {0}", message);
            }
        }

        public void Send(Message message)
        {
            Send(message.ToString());
        }

        private void OnSend(IAsyncResult ar)
        {
            try
            {
                // Complete sending the data to the remote device. 
                _tcpStream.EndWrite(ar);
            }
            catch (Exception e)
            {
                Debug.LogWarningFormat("Failed to send: {0}", e);
            }
        }

        private void OnConnect(IAsyncResult ar)
        {
            try
            {
                // Retrieve the socket from the state object.  
                var client = (TcpClient)ar.AsyncState;

                // Complete the connection.  
                client.EndConnect(ar);

                _tcpStream = _tcpClient.GetStream();
                
                // Signal that the connection has been made.  
                Debug.Log("Connected");

                _listenThread = new Thread(Listen);
                _listenThread.Start();
            }
            catch (Exception e)
            {
                Debug.LogWarningFormat("Error connecting to server: {0}", e.ToString());
            }
        }

        public void Dispatch(System.Action action)
        {
            lock (_dispatchLock)
            {
                _dispatchList.Add(action);
                _dispatching = true;
            }   
        }

        public void StartQueue(string ship, string weapon)
        {
            var msg = new Message(Protocol.MsgDomainLobby, Protocol.MsgCliQueueStart, "Start queue");
            msg.Body[Protocol.KeyShip] = ship;
            msg.Body[Protocol.KeyWeapon] = weapon;
            Send(msg);
        }

        public void StopQueue()
        {
            Send(new Message(Protocol.MsgDomainLobby, Protocol.MsgCliQueueStop, "Stop queue"));
        }

        void Update ()
        {
            if (!_dispatching)
                return;

            lock (_dispatchLock)
            {
                _dispatchListCopy.AddRange(_dispatchList);
                _dispatchList.Clear();
            }

            foreach (var action in _dispatchListCopy)
            {
                action.Invoke();
            }

            _dispatchListCopy.Clear();
        }

        void OnApplicationQuit()
        {
            _tcpClient.Close();
        }

        void OnGUI()
        {
            if (GUI.Button(new Rect(10, 10, 150, 100), "QUEUE"))
            {
                StartQueue("tank", "laser");
            }
        }
    }
}
