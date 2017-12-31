using System;
using System.Collections.Generic;
using System.Linq;
using Assets.Scripts.Data;
using Assets.Scripts.Utils;
using Protocol;
using UnityEngine;

namespace Assets.Scripts
{
    public class BattleManager : Singleton<BattleManager>
    {
        private string _cheatCardName;

        public Side MySide
        {
            get { return Client.Instance.Side; }
        }
        public Side OpponentsSide
        {
            get { return MySide == Side.A ? Side.B : Side.A; }
        }

        public EntityState MyState
        {
            get
            {
                return PlayerEntityState(Perspective.My);
            }
        }

        public EntityState OpponentsState
        {
            get { return PlayerEntityState(Perspective.Opponent); }
        }

        public event Action<GameState> StateUpdated;

        public EntitiesAppearence EntitiesAppearence;

        private GameState _state;
        private readonly List<Entity> _entities = new List<Entity>();

        void Start ()
        {
            Client.Instance.GameMessageReceived += OnGameMessageReceived;
            StateUpdated += OnStateUpdated;
        }

        private void OnStateUpdated(GameState newState)
        {
            var myState = MyState;
            if (myState != null)
                UpdatePlayerEntity(myState);

            var opState = OpponentsState;
            if (opState != null)
                UpdatePlayerEntity(opState);

            var objectIds = new List<int>{0, 1};
            var objects = newState.Objects;
            if (objects != null)
            {
                foreach (var entityState in objects)
                {
                    var id = entityState.Id;
                    objectIds.Add(id);
                    var existing = _entities.FirstOrDefault(e => e.Id == id);
                    if (existing == null)
                    {
                        var ei = EntitiesAppearence.GetPrefab(entityState.Name);
                        SpawnEntity(ei, entityState);
                    }
                    else
                    {
                        existing.UpdateState(entityState);
                    }
                }
            }

            
            var eToRemove = _entities.Where(e => !objectIds.Contains(e.Id));
            foreach (var e in eToRemove)
                e.DestroyEntity();

            _entities.RemoveAll(e => !objectIds.Contains(e.Id));
        }

        private void UpdatePlayerEntity(EntityState state)
        {
            var entityId = state.Id;
            var existing = _entities.FirstOrDefault(e => e.Id == entityId);
            if (existing == null)
            {
                var shipName = state.ShipName;
                var ei = EntitiesAppearence.GetPrefab(shipName);
                SpawnEntity(ei, state);
            }
            else
            {
                existing.UpdateState(state);
            }
        }

        public void SpawnEntity(GameObject prefab, EntityState state)
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

            var state = message.Game.State;
            if (state != null)
            {
                _state = state;
                
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
            var message = new Message()
            {
                Domain = Domain.Game,
                Head = Head.CliGameAction,
                Status = "Fire weapon",
                Game =
                {
                    GameId = Client.Instance.GameId,
                    Action =
                    {
                        Action = PlayerAction.FireWeapon
                    }
                }
            };
            Client.Instance.Send(message);
        }

        public void PlayCard(string cardId)
        {
            var message = new Message()
            {
                Domain = Domain.Game,
                Head = Head.CliGameAction,
                Status = "Play card",
                Game =
                {
                    GameId = Client.Instance.GameId,
                    Action =
                    {
                        Action = PlayerAction.FireWeapon,
                        Card = cardId
                    }
                }
            };
            Client.Instance.Send(message);
        }

        public void EndTurn()
        {
            var message = new Message()
            {
                Domain = Domain.Game,
                Head = Head.CliGameAction,
                Status = "Play card",
                Game =
                {
                    GameId = Client.Instance.GameId,
                    Action =
                    {
                        Action = PlayerAction.EndTurn,
                    }
                }
            };
            Client.Instance.Send(message);
        }

        public void CheatGainCard(string cardId)
        {
            if(string.IsNullOrEmpty(_cheatCardName))
                return;

            var message = new Message()
            {
                Domain = Domain.Game,
                Head = Head.CliGameAction,
                Status = "Take cheat card",
                Game =
                {
                    GameId = Client.Instance.GameId,
                    Action =
                    {
                        Action = PlayerAction.CheatGainCard,
                        Card = cardId
                    }
                }
            };
            
            Client.Instance.Send(message);
        }

        public EntityState PlayerEntityState(Perspective perspective = Perspective.My)
        {
            if (_state == null)
                return null;

            if (perspective == Perspective.My)
                return _state.Objects.FirstOrDefault(e => e.IsPlayer && e.Side == MySide);
            
            if (perspective == Perspective.Opponent)
                return _state.Objects.FirstOrDefault(e => e.IsPlayer && e.Side == OpponentsSide);

            return null;
        }

        public EntityState GetEntityState(int id)
        {
            return _state.Objects.FirstOrDefault(entityState => id == entityState.Id);
        }

        public bool IsOffense(Perspective perspective)
        {
            if (perspective == Perspective.My)
                return MyState.Position < OpponentsState.Position;

            return MyState.Position > OpponentsState.Position;
        }

#if DEBUG
        void OnGUI()
        {
            _cheatCardName = GUI.TextField(new Rect(30, 0, 100, 20), _cheatCardName);
            if (GUI.Button(new Rect(130, 0, 80, 20), "Take"))
            {
                CheatGainCard(_cheatCardName);
            }
        }
#endif
    }
}
