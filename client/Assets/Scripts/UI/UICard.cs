using Assets.Scripts.Data;
using SimpleJSON;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    [RequireComponent(typeof(Button))]
    public class UICard : MonoBehaviour
    {
        public CardsAppearance Appearance;
        public Image Background;
        public Image ActionTypeIcon;
        public Text NameText;
        public Text CostText;

        public float SmoothTime = 0.1f;
        public bool FollowMouse = false;

        private string _name;
        private Button _button;

        private Vector3 _target = new Vector3(0, 0, 0);
        private float _targetRotation = 0f;
        private RectTransform _rectTransform;
        private Vector3 _velocity;
        private float _velocityRotation;
        

        void Start ()
        {
            _button = GetComponent<Button>();
            _button.onClick.AddListener(new UnityAction(() =>
            {
                if(!string.IsNullOrEmpty(_name))
                    BattleManager.Instance.PlayCard(_name);
            }));

            /*
            _rectTransform = GetComponent<RectTransform>();
            _target = _rectTransform.position;
            _targetRotation = _rectTransform.eulerAngles.z;


            SetTarget(new Vector3(0, 0, 0), 0);
            */
        }
	
        void Update ()
        {
            /*
            _rectTransform.position = Vector3.SmoothDamp(_rectTransform.position, _target, ref _velocity, SmoothTime);
            var zAngle = Mathf.SmoothDampAngle(transform.eulerAngles.z, _targetRotation, ref _velocityRotation, SmoothTime);
            _rectTransform.eulerAngles = new Vector3(0, 0, zAngle);

            if (FollowMouse)
            {
                SetTarget(Input.mousePosition, -_velocity.x * 0.02f);
            }  */ 
        }

        void SetTarget(Vector3 target, float targetRotation)
        {
            _target = target;
            _targetRotation = targetRotation;
        }

        public void UpdateState(JSONObject cardState, bool isOffense)
        {
            var cardName = cardState[Rules.PStateCardName].Value;
            _name = cardName;

            var cardInfo = Client.Instance.GetCard(cardName);

            if (NameText != null)
                NameText.text = cardInfo[Rules.PCardFullName];

            if (CostText != null)
            {
                if (isOffense)
                    CostText.text = cardState[Rules.PStateCardCostOffense].AsInt.ToString();
                else
                    CostText.text = cardState[Rules.PStateCardCostDefense].AsInt.ToString();
            }

            if (ActionTypeIcon != null)
            {
                if (isOffense)
                    ActionTypeIcon.sprite = Appearance.OffenseIcon;
                else
                    ActionTypeIcon.sprite = Appearance.DefenseIcon;
            }

            if (Background != null)
            {
                Background.color = Appearance.GetColorForType(cardInfo[Rules.PCardType].Value);
            }

            //var actionKey = isOffense ? Rules.PCardActionOffense : Rules.PCardActionDefense;
            //var action = cardInfo

            /*
            var shaker = GetComponent<UIShaker>();
            if (shaker != null)
                shaker.Shake();*/
        }

        void OnMouseOver()
        {
            Debug.Log("MOUSE OVER");
        }
    }
}
