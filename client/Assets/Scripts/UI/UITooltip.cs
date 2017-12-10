using Assets.Scripts.Utils;
using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    [RequireComponent(typeof(CanvasGroup))]
    public class UITooltip : Singleton<UITooltip>
    {
        public Text Header;
        public Text Message;

        private CanvasGroup _canvasGroup;
        private bool _isShowing = true;
        
        void Start ()
        {
            _canvasGroup = GetComponent<CanvasGroup>();
            Hide();
        }
	
        void Update ()
        {
            var mouse = Input.mousePosition;

            if (_isShowing)
            {
                var w = ((RectTransform)transform).rect.width;
                var h = ((RectTransform)transform).rect.height;

                if (mouse.y < h)
                {
                    transform.position = new Vector3(mouse.x, h / 2, 0);
                }
                else
                {
                    transform.position = mouse;
                }
            }
        }

        public void Show(string header, string message)
        {
            if (Header != null)
                Header.text = header;

            if (Message != null)
                Message.text = message;

            _canvasGroup.alpha = 1f;
            _canvasGroup.blocksRaycasts = false;
            _canvasGroup.interactable = false;

            _isShowing = true;
        }

        public void Hide()
        {
            if (_isShowing)
            {
                _canvasGroup.alpha = 0f;
                _canvasGroup.blocksRaycasts = false;
                _canvasGroup.interactable = false;

                _isShowing = false;
            }
        }
    }
}
