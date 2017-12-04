using UnityEngine;

namespace Assets.Scripts
{
    public class Floater : MonoBehaviour
    {
        public float XAmplitude = 0.1f;
        public float YAmplitude = 0.05f;
        public float RotAmplitude = 0.1f;

        private float _mod;
        private float _offset;

        void Start ()
        {
            _offset = Random.value * Mathf.PI * 2;
            _mod = 0.9f + 0.2f * Random.value;
        }
	
        
        void Update ()
        {
            var pos = transform.position;
            var xv = Mathf.Sin(Time.time * _mod + _offset);
            pos.x = XAmplitude * xv;
            pos.y = YAmplitude * Mathf.Sin(Time.time * _mod * 2 + _offset);
            transform.position = pos;

            transform.Rotate(0, 0, RotAmplitude * xv);
        }
    }
}
