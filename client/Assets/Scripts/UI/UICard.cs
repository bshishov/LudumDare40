using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    public class UICard : MonoBehaviour
    {
        public float SmoothTime = 0.1f;
        public bool FollowMouse = false;

        private Vector3 _target = new Vector3(0, 0, 0);
        private float _targetRotation = 0f;
        private RectTransform _rectTransform;
        private Vector3 _velocity;
        private float _velocityRotation;
        private Canvas _canvas;

        void Start ()
        {
            _rectTransform = GetComponent<RectTransform>();
            _target = _rectTransform.position;
            _targetRotation = _rectTransform.eulerAngles.z;
            _canvas = FindObjectOfType<Canvas>();


            SetTarget(new Vector3(0, 0, 0), 0);
        }
	
        void Update ()
        {
            _rectTransform.position = Vector3.SmoothDamp(_rectTransform.position, _target, ref _velocity, SmoothTime);
            var zAngle = Mathf.SmoothDampAngle(transform.eulerAngles.z, _targetRotation, ref _velocityRotation, SmoothTime);
            _rectTransform.eulerAngles = new Vector3(0, 0, zAngle);

            if (FollowMouse)
            {
                SetTarget(Input.mousePosition, -_velocity.x * 0.02f);
            }   
        }

        void SetTarget(Vector3 target, float targetRotation)
        {
            _target = target;
            _targetRotation = targetRotation;
        }
    }
}
