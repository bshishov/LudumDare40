using UnityEngine;

namespace Assets.Scripts
{
    public class CloudArray : MonoBehaviour
    {
        public GameObject[] Cloud2s;
        public Vector3 Direction = Vector3.left;
        public float LifeTime = 2f;
        public float DelayFrom = 0.1f;
        public float DelayTo = 0.5f;

        private float _t = 0f;
        private float _nextDelay = 0f;

        void Start ()
        {
		    
        }
	
        void Update ()
        {
            _t += Time.deltaTime;
            if (_t > _nextDelay)
            {
                Spawn();
                _nextDelay = Random.Range(DelayFrom, DelayTo);
                _t = 0;
            }
        }

        void Spawn()
        {
            
        }
    }
}
