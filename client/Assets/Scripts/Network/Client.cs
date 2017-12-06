using System;
using System.Collections.Generic;
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
            get { return _channel != null && _channel.IsConnected; }
        }

        public bool IsInGame { get; private set; }
        public bool IsInQueue { get; private set; }
        public string GameId { get; private set; }
        public string Side { get; private set; }
        
        public string Host = "127.0.0.1";
        public int Port = 8976;
        public string GameSceneName = "Battle";
        public string LobbySceneName = "Lobby";

        public event Messagehandler MessageReceived;
        public event Messagehandler GameMessageReceived;
        public event Messagehandler LobbyMessageReceived;
        
        private readonly Dictionary<string, List<Messagehandler>> _messageSubscribers = 
            new Dictionary<string, List<Messagehandler>>(); 

        // Dispatching
        private readonly List<System.Action> _dispatchList = new List<Action>();
        private readonly List<System.Action> _dispatchListCopy = new List<Action>();
        private bool _dispatching;
        private readonly object _dispatchLock = new object();

        private readonly NetworkChannel<Message> _channel = 
            new NetworkChannel<Message>(new MessageSerializer());


        void Awake()
        {
            DontDestroyOnLoad(gameObject);
        }

        void Start ()
        {
            _channel.Start(Host, Port);
            _channel.Received += (ch, msg) =>
            {
                // Dispatch message processing to Unity thread
                if (MessageReceived != null)
                    Dispatch(() => MessageReceived.Invoke(msg));
            };

            
            _channel.ErrorOccured += (ch, err) =>
            {
                Debug.LogWarningFormat("Channel error: {0}", err);
                if (SceneManager.GetActiveScene().name != LobbySceneName)
                    SceneManager.LoadScene(LobbySceneName);
            };

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
                SceneManager.LoadScene(GameSceneName);
            });

            Subscribe(Protocol.MsgSrvGameEffect, message =>
            {
                Debug.LogFormat("Effect: {0}", message);
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
        
        public void Send(Message message)
        {
            _channel.Send(message);
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
            _channel.Close();
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
