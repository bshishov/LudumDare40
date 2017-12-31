using System.Collections.Generic;
using Assets.Scripts.Data;
using Protocol;
using UnityEngine;

namespace Assets.Scripts.UI
{
    public class UIBuffCollection : MonoBehaviour
    {
        public GameObject BuffPrefab;
        public Perspective Perspective;
        public int EntityId;

        private readonly List<UIBuff> _buffs = new List<UIBuff>();
        
        void Start ()
        {
            BattleManager.Instance.StateUpdated += OnStateUpdated;
        }

        private void OnStateUpdated(GameState gameState)
        {
            var state = GetEntityState();
            if(state == null)
                return;

            foreach (var b in _buffs)
                Destroy(b.gameObject);

            _buffs.Clear();

            foreach (var buffState in state.Buffs)
            {
                AddBuff(buffState);
            }
        }

        private void AddBuff(BuffState buffState)
        {
            var go = (GameObject)GameObject.Instantiate(BuffPrefab, transform);
            var buff = go.GetComponent<UIBuff>();
            buff.UpdateState(buffState);
            _buffs.Add(buff);
        }

        private EntityState GetEntityState()
        {
            if (Perspective == Perspective.Neutral)
                return BattleManager.Instance.GetEntityState(EntityId);

            return BattleManager.Instance.PlayerEntityState(Perspective);
        }
    }
}
