using UnityEngine;

namespace Assets.Scripts.UI
{
    [RequireComponent(typeof(RectTransform))]
    public class UIShaker : MonoBehaviour
    {
        public float Amplitude = 4f;
        public float Speed = 70f;

        private bool _isShaking;
        private RectTransform _rectTransform;
        private float _timeRemaining;
        private Vector3 _rotationBeforeShaking;
        
        void Start ()
        {
            _rectTransform = GetComponent<RectTransform>();
        }

      
        void Update ()
        {
            if (_isShaking)
            {
                _timeRemaining -= Time.deltaTime;
                if (_timeRemaining < 0f)
                {
                    _isShaking = false;
                    _rectTransform.eulerAngles = _rotationBeforeShaking;
                }
                else
                {
                    _rectTransform.eulerAngles = _rotationBeforeShaking + new Vector3(0, 0, Mathf.Sin(Time.time * Speed) * Amplitude);
                }
            }
        }

        public void Shake(float duration=0.5f)
        {
            if(!_isShaking)
                _rotationBeforeShaking = _rectTransform.eulerAngles;
            _isShaking = true;
            _timeRemaining = duration;
        }
    }
}
