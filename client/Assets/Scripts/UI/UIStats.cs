using SimpleJSON;
using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    public class UIStats : MonoBehaviour
    {
        public Perspective Perspective;
        public Text HpText;
        public Text EnergyText;
        public Text EnergyGainText;
        
        void Start ()
        {
            BattleManager.Instance.StateUpdated += OnStateUpdated;
        }

        private void OnStateUpdated(JSONObject obj)
        {
            var state = BattleManager.Instance.StateForPerspective(Perspective);
            var hp = state[Rules.PStateHp].AsInt;
            var energy = state[Rules.PStateEnergy].AsInt;
            var energyMax = state[Rules.PStateMaxEnergy].AsInt;
            var energyGain = state[Rules.PStateEnergyGain].AsInt;

            if (HpText != null)
                HpText.text = hp.ToString();

            if (EnergyText != null)
                EnergyText.text = string.Format("{0}/{1}", energy, energyMax);

            if (EnergyGainText != null)
                EnergyGainText.text = energyGain.ToString("+0;-#");

            var shaker = GetComponent<UIShaker>();
            if (shaker != null)
                shaker.Shake();
        }
    }
}
