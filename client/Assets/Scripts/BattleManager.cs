using System;
using Assets.Scripts.Network;
using Assets.Scripts.Utils;
using SimpleJSON;
using UnityEngine;

namespace Assets.Scripts
{
    public class BattleManager : Singleton<BattleManager>
    {
        public string MySide
        {
            get { return Client.Instance.Side; }
        }
        public string OpponentsSide
        {
            get { return MySide == Rules.SideA ? Rules.SideB : Rules.SideA; }
        }

        public event Action<JSONObject> StateUpdated;

        private JSONObject _state;

        void Start ()
        {
            Client.Instance.GameMessageReceived += InstanceOnGameMessageReceived;
        }

        private void InstanceOnGameMessageReceived(Message message)
        {
            var state = message.Body[Protocol.KeyState];
            if (state != null)
            {
                _state = state.AsObject;
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
                Client.Instance.GameMessageReceived -= InstanceOnGameMessageReceived;
        }

        public void FireWeapon()
        {
            var m = new Message(Protocol.MsgDomainGame, Protocol.MsgCliGameAction, "Fire weapon");
            m.Body[Rules.PType] = Rules.ActionFireWeapon;
            m.Body[Protocol.KeyGameId] = Client.Instance.GameId;
            Client.Instance.Send(m);
        }

        public void PlayCard(string cardId)
        {
            var m = new Message(Protocol.MsgDomainGame, Protocol.MsgCliGameAction, "Play card");
            m.Body[Rules.PType] = Rules.ActionPlayCard;
            m.Body["card"] = Rules.ActionPlayCard;
            m.Body[Protocol.KeyGameId] = Client.Instance.GameId;
            Client.Instance.Send(m);
        }

        public void EndTurn()
        {
            var m = new Message(Protocol.MsgDomainGame, Protocol.MsgCliGameAction, "End turn");
            m.Body[Rules.PType] = Rules.ActionEndTurn;
            m.Body[Protocol.KeyGameId] = Client.Instance.GameId;
            Client.Instance.Send(m);
        }
    }
}
