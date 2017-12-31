using Protocol;
using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    public class UIEntity : MonoBehaviour
    {
        public UIBuffCollection BuffCollection;
        public Text HpText;
        public Text EnergyText;


        public void UpdateState(EntityState state)
        {
            if(state == null)
                return;

            if (HpText != null)
                HpText.text = state.Hp.ToString();

            if (EnergyText != null)
                EnergyText.text = state.Energy.ToString();

            var shaker = GetComponent<UIShaker>();
            if(shaker != null)
                shaker.Shake();

            if(BuffCollection != null)
                BuffCollection.EntityId = state.Id;
        }
    }
}
