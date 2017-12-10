using SimpleJSON;
using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    public class UIEntity : MonoBehaviour
    {
        public UIBuffCollection BuffCollection;
        public Text HpText;
        public Text EnergyText;


        public void UpdateState(JSONObject entityState)
        {
            if(entityState == null)
                return;

            if (HpText != null)
                HpText.text = entityState[Rules.PStateHp];

            if (EnergyText != null)
                EnergyText.text = entityState[Rules.PStateEnergy];

            var shaker = GetComponent<UIShaker>();
            if(shaker != null)
                shaker.Shake();

            if(BuffCollection != null)
                BuffCollection.EntityId = entityState[Rules.PStateId].AsInt;
        }
    }
}
