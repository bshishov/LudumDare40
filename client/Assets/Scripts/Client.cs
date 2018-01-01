using System;
using System.Collections.Generic;
using Assets.Scripts.Network;
using Assets.Scripts.Utils;
using Protocol;
using SimpleJSON;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace Assets.Scripts
{
    [RequireComponent(typeof(ActionDispatcher))]
    public class Client : Singleton<Client>
    {
        public delegate void Messagehandler(Message message);

        public bool IsActive
        {
            get { return _channel != null && _channel.IsConnected; }
        }

        public bool IsInGame { get; private set; }
        public bool IsGameStarted { get; private set; }
        public bool IsInQueue { get; private set; }
        public string GameId { get; private set; }
        public Side Side { get; private set; }
        
        public string Host = "127.0.0.1";
        public int Port = 8976;
        public string GameSceneName = "Battle";
        public string LobbySceneName = "Lobby";
        public TextAsset GameDbAsset;

        public event Messagehandler MessageReceived;
        public event Messagehandler GameMessageReceived;
        public event Messagehandler LobbyMessageReceived;
        
        private readonly Dictionary<Head, List<Messagehandler>> _messageSubscribers = 
            new Dictionary<Head, List<Messagehandler>>(); 

        private readonly NetworkChannel<Message> _channel = 
            new NetworkChannel<Message>(new MessageSerializer());

        private JSONNode _db;
        private ActionDispatcher _dispatcher;


        void Awake()
        {
            DontDestroyOnLoad(gameObject);
        }

        void Start ()
        {
            _dispatcher = GetComponent<ActionDispatcher>();

            // Load database
            if (GameDbAsset == null)
            {
                Debug.LogError("Game DB asset is not set");
            }
            else
            {
                _db = JSON.Parse(GameDbAsset.text);
                Debug.LogFormat("Loaded Game DB asset: Length: {0}", GameDbAsset.text.Length);
            }

            _channel.Start(Host, Port);
            _channel.Received += (ch, msg) =>
            {
                // Dispatch message processing to Unity thread
                if (MessageReceived != null)
                    _dispatcher.Dispatch(() => MessageReceived.Invoke(msg));
            };
            
            _channel.ErrorOccured += (ch, err) =>
            {
                _dispatcher.Dispatch(() => OnChannelError(err));
            };

            MessageReceived += OnMessageReceive;

            Subscribe(Head.SrvHello, message =>
            {
                Debug.LogFormat("Hello: {0}", message);
            });

            Subscribe(Head.SrvGameStarted, message =>
            {
                IsGameStarted = true;
                Side = message.Game.YourSide;
                Debug.LogFormat("Game begin, side: {0}", Side);
            });

            Subscribe(Head.SrvQueueStarted, message =>
            {
                IsInQueue = true;
                Debug.Log("Queue started");
            });

            Subscribe(Head.SrvQueueStopped, message =>
            {
                IsInQueue = false;
                Debug.Log("Queue stopped");
            });

            Subscribe(Head.SrvQueueGameCreated, message =>
            {
                IsInQueue = false;
                IsInGame = true;
                GameId = message.GameCreated.GameId;
                Debug.LogFormat("Game started, id: {0}", GameId);
                if(SceneManager.GetActiveScene().name != GameSceneName)
                    SceneManager.LoadScene(GameSceneName);
            });

            Subscribe(Head.SrvGameEffect, message =>
            {
                Debug.LogFormat("Effect: {0}", message);
            });

            Subscribe(Head.SrvGameEnded, message =>
            {
                IsInGame = false;
                IsGameStarted = false;
                Debug.LogFormat("Game ended: {0}", message);
            });
        }

        private void OnMessageReceive(Message message)
        {
            // Message domain dispatching
            if (message.Domain == Domain.Lobby)
            {
                if(LobbyMessageReceived != null)
                    LobbyMessageReceived.Invoke(message);
            }
            else if (message.Domain == Domain.Game)
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

        private void OnChannelError(Exception err)
        {
            IsInGame = false;
            IsGameStarted = false;
            IsInQueue = false;
            Debug.LogWarningFormat("Channel error: {0}", err);
            if (SceneManager.GetActiveScene().name != LobbySceneName)
                SceneManager.LoadScene(LobbySceneName);
        }

        public void Subscribe(Head head, Messagehandler handler)
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

        public void UnSubscribe(Head head, Messagehandler handler)
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

        public void StartQueue(string ship, string weapon)
        {
            var msg = new Message
            {
                Domain = Domain.Lobby,
                Head = Head.CliQueueStart,
                QueuePrefs = new CliQueuePreferences
                {
                    Ship = ship,
                    Weapon = weapon
                }
            }; 
            Send(msg);
        }

        public void StopQueue()
        {
            var message = new Message()
            {
                Domain = Domain.Lobby,
                Head = Head.CliQueueStop
            };
            Send(message);
        }

        void OnApplicationQuit()
        {
            _channel.Close();
        }

        public JSONObject GetCard(string key)
        {
            return _db[Rules.SectionCards][key].AsObject;
        }

        void OnGUI()
        {
            if (GUI.Button(new Rect(0, 0, 30, 20), "FL"))
                StartQueue("fighter", "laser");

            if (GUI.Button(new Rect(0, 20, 30, 20), "FH"))
                StartQueue("fighter", "harpoon");

            if (GUI.Button(new Rect(0, 40, 30, 20), "FM"))
                StartQueue("fighter", "mg");

            if (GUI.Button(new Rect(0, 60, 30, 20), "TL"))
                StartQueue("tank", "laser");

            if (GUI.Button(new Rect(0, 80, 30, 20), "TH"))
                StartQueue("tank", "harpoon");

            if (GUI.Button(new Rect(0, 100, 30, 20), "TM"))
                StartQueue("tank", "mg");

            if (GUI.Button(new Rect(0, 120, 30, 20), "SL"))
                StartQueue("scout", "laser");

            if (GUI.Button(new Rect(0, 140, 30, 20), "SH"))
                StartQueue("scout", "harpoon");

            if (GUI.Button(new Rect(0, 160, 30, 20), "SM"))
                StartQueue("scout", "mg");           
        }

        public JSONObject GetWeapon(string key)
        {
            return _db[Rules.SectionWeapons][key].AsObject;
        }
    }
}
