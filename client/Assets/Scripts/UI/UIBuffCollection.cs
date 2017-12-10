using System.Collections.Generic;
using SimpleJSON;
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

        private void OnStateUpdated(JSONObject gameState)
        {
            var state = GetEntityState();
            if(state == null)
                return;

            foreach (var b in _buffs)
                Destroy(b.gameObject);

            _buffs.Clear();

            var buffs = state[Rules.PStateBuffs];
            foreach (var buffState in buffs.Children)
            {
                AddBuff(buffState.AsObject);
            }
        }

        private void AddBuff(JSONObject buffState)
        {
            var go = (GameObject)GameObject.Instantiate(BuffPrefab, transform);
            var buff = go.GetComponent<UIBuff>();
            buff.UpdateState(buffState);
            _buffs.Add(buff);
        }

        private JSONObject GetEntityState()
        {
            if (Perspective == Perspective.Neutral)
                return BattleManager.Instance.GetEntityState(EntityId);

            return BattleManager.Instance.StateForPerspective(Perspective);
        }
    }
}
