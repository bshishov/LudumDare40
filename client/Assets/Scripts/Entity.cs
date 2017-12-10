using SimpleJSON;
using UnityEngine;

namespace Assets.Scripts
{
    public class Entity : MonoBehaviour
    {
        public int Id { get { return _state[Rules.PStateId]; } }
        public float MoveSpeed = 1f;

        private JSONObject _state;
        private Vector3 _velocity;
        private Vector3 _target;

        void Start ()
        {
        }

        void Update()
        {
            transform.position = Vector3.SmoothDamp(transform.position, _target, ref _velocity, MoveSpeed);
        }

        public void MoveTo(int position)
        {
            _target = GameToWorldPosition(position);
        }

        public void UpdateState(JSONObject eState)
        { 
            var position = eState[Rules.PStatePosition].AsInt;
            MoveTo(position);

            if (_state == null)
            {
                transform.position = GameToWorldPosition(position);
                _target = GameToWorldPosition(position);
            }

            _state = eState;
        }

        private Vector3 GameToWorldPosition(int position)
        {
            return new Vector3(0, 0, position);
        }
    }
}
