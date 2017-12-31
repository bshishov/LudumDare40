using Assets.Scripts.Data;
using Protocol;
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

        private BuffState _state;

        void Start ()
        {
        }

        public void UpdateState(BuffState buffState)
        {

            if (Icon != null)
                Icon.sprite = Appearance.GetIcon(buffState.Name);

            if (Duration != null)
                Duration.text = buffState.Duration.ToString();

            _state = buffState;
        }

        public void OnPointerEnter(PointerEventData eventData)
        {
            var tooltip = UITooltip.Instance;
            if (tooltip != null)
                tooltip.Show("Buff", _state.ToString());
        }

        public void OnPointerExit(PointerEventData eventData)
        {
            var tooltip = UITooltip.Instance;
            if (tooltip != null)
                tooltip.Hide();
        }
    }
}
