using Assets.Scripts.Data;
using Protocol;
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

        private void OnStateUpdated(GameState gameState)
        {
            var state = BattleManager.Instance.PlayerEntityState(Perspective);
            var hp = state.Hp;
            var energy = state.Energy;
            var energyMax = state.MaxEnergy;
            var energyGain = state.EnergyGain;

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
