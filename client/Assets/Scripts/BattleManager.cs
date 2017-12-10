using System;
using System.Collections.Generic;
using System.Linq;
using Assets.Scripts.Data;
using Assets.Scripts.Network;
using Assets.Scripts.UI;
using Assets.Scripts.Utils;
using SimpleJSON;
using UnityEngine;

namespace Assets.Scripts
{
    public class BattleManager : Singleton<BattleManager>
    {
        private string _cheatCardName;

        public string MySide
        {
            get { return Client.Instance.Side; }
        }
        public string OpponentsSide
        {
            get { return MySide == Rules.SideA ? Rules.SideB : Rules.SideA; }
        }

        public JSONObject MyState
        {
            get
            {
                return StateForPerspective(Perspective.My);
            }
        }

        public JSONObject OpponentsState
        {
            get { return StateForPerspective(Perspective.Opponent); }
        }

        public event Action<JSONObject> StateUpdated;

        public EntitiesAppearence EntitiesAppearence;

        private JSONObject _state;
        private readonly List<Entity> _entities = new List<Entity>();

        void Start ()
        {
            Client.Instance.GameMessageReceived += OnGameMessageReceived;
            StateUpdated += OnStateUpdated;
        }

        private void OnStateUpdated(JSONObject newState)
        {
            var myState = MyState;
            if (myState != null)
                UpdatePlayerEntity(myState);

            var opState = OpponentsState;
            if (opState != null)
                UpdatePlayerEntity(opState);

            var objectIds = new List<int>{0, 1};
            var objects = newState[Rules.PStateObjects];
            if (objects != null)
            {
                foreach (var o in objects.Children)
                {
                    var id = o[Rules.PStateId].AsInt;
                    objectIds.Add(id);
                    var existing = _entities.FirstOrDefault(e => e.Id == id);
                    if (existing == null)
                    {
                        var ename = o[Rules.PStateName].Value;
                        var ei = EntitiesAppearence.GetPrefab(ename);
                        SpawnEntity(ei, o.AsObject);
                    }
                    else
                    {
                        existing.UpdateState(o.AsObject);
                    }
                }
            }

            _entities.RemoveAll(e => !objectIds.Contains(e.Id));
        }

        private void UpdatePlayerEntity(JSONObject state)
        {
            var entityId = state[Rules.PStateId];
            var existing = _entities.FirstOrDefault(e => e.Id == entityId);
            if (existing == null)
            {
                var shipName = state[Rules.PStateShipName].Value;
                var ei = EntitiesAppearence.GetPrefab(shipName);
                SpawnEntity(ei, state);
            }
            else
            {
                existing.UpdateState(state);
            }
        }

        public void SpawnEntity(GameObject prefab, JSONObject state)
        {
            var go = (GameObject)GameObject.Instantiate(prefab, Vector3.zero, Quaternion.identity);
            var entity = go.GetComponent<Entity>();
            if (entity == null)
                entity = go.AddComponent<Entity>();
            entity.UpdateState(state);
            _entities.Add(entity);
        }

        private void OnGameMessageReceived(Message message)
        {
            if (!Client.Instance.IsGameStarted)
                return;

            var state = message.Body[Protocol.KeyState];
            if (state != null)
            {
                _state = state.AsObject;
                
                // TODO: CHECK CONDITION
                if (StateUpdated != null)
                    StateUpdated.Invoke(_state);
            }
        }

        void Update ()
        {
        }

        void OnDestroy()
        {
            if(Client.Instance != null)
                Client.Instance.GameMessageReceived -= OnGameMessageReceived;
        }

        public void FireWeapon()
        {
            var m = new Message(Protocol.MsgDomainGame, Protocol.MsgCliGameAction, "Fire weapon");
            m.Body[Protocol.KeyGameId] = Client.Instance.GameId;
            m.Body["action"][Rules.PType] = Rules.ActionFireWeapon;
            Client.Instance.Send(m);
        }

        public void PlayCard(string cardId)
        {
            var m = new Message(Protocol.MsgDomainGame, Protocol.MsgCliGameAction, "Play card");
            m.Body["action"][Rules.PType] = Rules.ActionPlayCard;
            m.Body["action"]["card"] = cardId;
            m.Body[Protocol.KeyGameId] = Client.Instance.GameId;
            Client.Instance.Send(m);
        }

        public void EndTurn()
        {
            var m = new Message(Protocol.MsgDomainGame, Protocol.MsgCliGameAction, "End turn");
            m.Body["action"][Rules.PType] = Rules.ActionEndTurn;
            m.Body[Protocol.KeyGameId] = Client.Instance.GameId;
            Client.Instance.Send(m);
        }

        public void CheatGainCard()
        {
            if(string.IsNullOrEmpty(_cheatCardName))
                return;

            var m = new Message(Protocol.MsgDomainGame, Protocol.MsgCliGameAction, "Take card");
            m.Body["action"][Rules.PType] = Rules.ActionCheatTakeCard;
            m.Body["action"]["card"] = _cheatCardName;
            m.Body[Protocol.KeyGameId] = Client.Instance.GameId;
            Client.Instance.Send(m);
        }

        public JSONObject StateForPerspective(Perspective perspective)
        {
            if (_state == null)
                return null;

            if (string.IsNullOrEmpty(MySide))
                return null;

            if (perspective == Perspective.My)
                return _state[MySide].AsObject;

            if (perspective == Perspective.Opponent)
                return _state[OpponentsSide].AsObject;

            return null;
        }

        public bool IsOffense(Perspective perspective)
        {
            var myPos = MyState[Rules.PStatePosition].AsInt;
            var opponentsPos = OpponentsState[Rules.PStatePosition].AsInt;

            if (perspective == Perspective.My)
                return myPos < opponentsPos;

            return myPos > opponentsPos;
        }

#if DEBUG
        void OnGUI()
        {
            _cheatCardName = GUI.TextField(new Rect(30, 0, 100, 20), _cheatCardName);
            if (GUI.Button(new Rect(130, 0, 80, 20), "Take"))
            {
                CheatGainCard();
            }
        }
#endif
    }
}
