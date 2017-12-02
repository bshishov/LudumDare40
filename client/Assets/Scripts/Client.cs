using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using Assets.Scripts.Utils;
using UnityEngine;
using Newtonsoft.Json;

namespace Assets.Scripts
{
    public class Client : Singleton<Client>
    {
        public class Message
        {
            
        }

        public bool IsActive
        {
            get { return _tcpClient != null && _tcpClient.Connected && _tcpStream != null; }
        }

        public string Host = "127.0.0.1";
        public int Port = 8976;

        public event Action<Message> OnReceive;

        private TcpClient _tcpClient;
        private NetworkStream _tcpStream;
        private Thread _listenThread;
        private readonly byte[] _readBuffer = new byte[8192];

        // Dispatching
        private readonly List<System.Action> _dispatchList = new List<Action>();
        private readonly List<System.Action> _dispatchListCopy = new List<Action>();
        private bool _dispatching = false;
        private readonly System.Object _dispatchLock = new System.Object();
        

        void Start ()
        {
		    _tcpClient = new TcpClient();
            _tcpClient.BeginConnect(Host, Port, new AsyncCallback(OnConnect), _tcpClient);
        }

        private void Listen()
        {
            while (true)
            {
                try
                {
                    var bytesReceived = _tcpStream.Read(_readBuffer, 0, _readBuffer.Length);
                    var messageRaw = Encoding.UTF8.GetString(_readBuffer, 0, bytesReceived);
                    Debug.LogFormat("Received: {0}", messageRaw);
                    var msg = JsonConvert.DeserializeObject<Message>(messageRaw);
                    Debug.LogFormat("Received: {0}", msg);
                    if(OnReceive != null)
                        Dispatch(() => OnReceive.Invoke(msg));
                }
                catch (Exception e)
                {
                    Debug.LogWarning("Failed to recognize message: {0}", e);
                    throw;
                }
                
            }
        }

        public void Send(Message message)
        {
            if (_tcpClient != null && _tcpClient.Connected && _tcpStream != null)
            {
                var buffer = new byte[8192];
                _tcpStream.BeginWrite(buffer, 0, 100, OnSend, _tcpClient);
            }
        }

        public void Send(string message)
        {
            if (_tcpClient != null && _tcpClient.Connected && _tcpStream != null)
            {
                var buffer = Encoding.UTF8.GetBytes(message);
                _tcpStream.BeginWrite(buffer, 0, buffer.Length, OnSend, _tcpClient);
                Debug.LogFormat("Sent: {0}", message);
            }
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
                Send("{\"type\":\"queue\", \"status\":\"start\", \"body\": {}}");
        }
    }
}
