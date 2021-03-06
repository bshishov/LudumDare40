﻿using Assets.Scripts.UI;
using Protocol;
using UnityEngine;

namespace Assets.Scripts
{

    public class Entity : MonoBehaviour
    {
        public int Id { get { return _state.Id; } }

        public GameObject UIPrefab;
        public float MoveSpeed = 1f;

        private EntityState _state;
        private Vector3 _velocity;
        private Vector3 _target;

        private UIEntity _ui;

        void Start ()
        {
            if (UIPrefab != null)
            {
                var go = (GameObject) GameObject.Instantiate(UIPrefab, BattleUIManager.Instance.transform);
                _ui = go.GetComponent<UIEntity>();
                if (_ui != null)
                {
                    var follow = _ui.GetComponent<UIFollowSceneObject>();
                    follow.Target = gameObject;
                }
            }
            
        }

        void Update()
        {
            transform.position = Vector3.SmoothDamp(transform.position, _target, ref _velocity, MoveSpeed);
        }

        public void MoveTo(int position)
        {
            _target = GameToWorldPosition(position);
        }

        public void UpdateState(EntityState eState)
        { 
            var position = eState.Position;
            MoveTo(position);

            if (_state == null)
            {
                transform.position = GameToWorldPosition(position);
                _target = GameToWorldPosition(position);
            }
            UpdateUI(eState);

            _state = eState;
        }

        private void UpdateUI(EntityState state)
        {
            if(_ui == null)
                return;

            _ui.UpdateState(state);
        }

        private Vector3 GameToWorldPosition(int position)
        {
            return new Vector3(0, 0, position);
        }

        public void DestroyEntity()
        {
            Destroy(gameObject);
        }

        void OnDestroy()
        {
            if (_ui != null)
            {
                Destroy(_ui.gameObject);
            }
        }

        void OnMouseEnter()
        {
            var tooltip = UITooltip.Instance;
            if(tooltip != null)
                tooltip.Show("Entity", _state.ToString());
        }

        void OnMouseExit()
        {
            var tooltip = UITooltip.Instance;
            if (tooltip != null)
                tooltip.Hide();
        }
    }
}
