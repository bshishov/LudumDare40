using Assets.Scripts.Data;
using SimpleJSON;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    public class UIBuff : MonoBehaviour, 
        IPointerEnterHandler,
        IPointerExitHandler
    {
        public BuffAppearance Appearance;
        public Image Icon;
        public Text Duration;

        private JSONObject _state;

        void Start ()
        {
        }

        public void UpdateState(JSONObject buffState)
        {
            var buffName = buffState[Rules.PStateBuffName].Value;
            var duration = buffState[Rules.PStateBuffDuration].AsInt;

            if (Icon != null)
                Icon.sprite = Appearance.GetIcon(buffName);

            if (Duration != null)
                Duration.text = duration.ToString();

            _state = buffState;
        }

        public void OnPointerEnter(PointerEventData eventData)
        {
            var tooltip = UITooltip.Instance;
            if (tooltip != null)
                tooltip.Show("Buff", _state.ToString(4));
        }

        public void OnPointerExit(PointerEventData eventData)
        {
            var tooltip = UITooltip.Instance;
            if (tooltip != null)
                tooltip.Hide();
        }
    }
}
