using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    [RequireComponent(typeof(Button))]
    [RequireComponent(typeof(Image))]
    public class UIShipIcon : MonoBehaviour {

        public string ShipName;

        private Button _button;
        private Image _image;

        private float _crossFadeDuration = 0.5f;
        private readonly Color _selectedColor = Color.white;
        private readonly Color _unSelectedColor = new Color(0.5f, 0.5f, 0.5f);

        void Start()
        {
            _button = GetComponent<Button>();
            _image = GetComponent<Image>();
            _button.onClick.AddListener(() =>
            {
                LobbyUIManager.Instance.SelectShip(ShipName); ;
            });
        }


        public void SetInteractible(bool val = true)
        {
            _button.interactable = val;
        }

        public void SetSelected(bool val)
        {
            var targetColor = val ? _selectedColor : _unSelectedColor;
            _image.CrossFadeColor(targetColor, _crossFadeDuration, false, false, true);
        }
    }
}
