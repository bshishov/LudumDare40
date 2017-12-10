﻿using System;
using System.Collections.Generic;
using Assets.Scripts.Network;
using Assets.Scripts.Utils;
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
        public string Side { get; private set; }
        
        public string Host = "127.0.0.1";
        public int Port = 8976;
        public string GameSceneName = "Battle";
        public string LobbySceneName = "Lobby";
        public TextAsset GameDbAsset;

        public event Messagehandler MessageReceived;
        public event Messagehandler GameMessageReceived;
        public event Messagehandler LobbyMessageReceived;
        
        private readonly Dictionary<string, List<Messagehandler>> _messageSubscribers = 
            new Dictionary<string, List<Messagehandler>>(); 

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

            Subscribe(Protocol.MsgSrvHello, message =>
            {
                Debug.LogFormat("Hello: {0}", message);
            });

            Subscribe(Protocol.MsgSrvGameBegin, message =>
            {
                IsGameStarted = true;
                Side = message.Body[Protocol.KeySide].Value;
                Debug.LogFormat("Game begin, side: {0}", Side);
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
                GameId = message.Body[Protocol.KeyGameId].Value;
                Debug.LogFormat("Game started, id: {0}", GameId);
                if(SceneManager.GetActiveScene().name != GameSceneName)
                    SceneManager.LoadScene(GameSceneName);
            });

            Subscribe(Protocol.MsgSrvGameEffect, message =>
            {
                Debug.LogFormat("Effect: {0}", message);
            });

            Subscribe(Protocol.MsgSrvGameEnd, message =>
            {
                IsInGame = false;
                IsGameStarted = false;
                Debug.LogFormat("Game ended: {0}", message);
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

        private void OnChannelError(Exception err)
        {
            IsInGame = false;
            IsGameStarted = false;
            IsInQueue = false;
            Debug.LogWarningFormat("Channel error: {0}", err);
            if (SceneManager.GetActiveScene().name != LobbySceneName)
                SceneManager.LoadScene(LobbySceneName);
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
