using Assets.Scripts.Data;
using SimpleJSON;
using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    public class UIWeapon : MonoBehaviour
    {
        public Perspective Perspective;
        public Image Icon;
        public Text AttackText;
        public Text CostText;
        public WeaponsAppearance Appearance;

        private string _weaponName;

        void Start()
        {
            BattleManager.Instance.StateUpdated += OnStateUpdated;
        }

        private void OnStateUpdated(JSONObject state)
        {
            var s = BattleManager.Instance.StateForPerspective(Perspective);
            if (s == null)
                return;

            var weaponName = s[Rules.PStateWeaponName].Value;
            var damageMod = s[Rules.PStateDamageMod].AsInt;

            var weapon = Client.Instance.GetWeapon(weaponName);
            var baseDamage = 0;
            if (weapon != null)
            {
                var key = BattleManager.Instance.IsOffense(Perspective)
                    ? Rules.PWeaponActionOffense
                    : Rules.PWeaponActionDefense;

                var action = weapon[key];
                if (action == null)
                    action = weapon[Rules.PWeaponActionSame];

                
                foreach (var effect in action[Rules.PWeaponEffects].Children)
                {
                    if (effect[Rules.PEffectType] == Rules.EffectTypeDamage)
                    {
                        baseDamage = effect[Rules.PEffectValue].AsInt;
                        break;
                    }
                }

                var cost = action[Rules.PWeaponCost].AsInt;

                if (CostText != null)
                    CostText.text = cost.ToString();
            }

            if (damageMod > 0)
                AttackText.text = string.Format("{0}<color=green>{1:+0;-#}</color>", baseDamage, damageMod);
            else if (damageMod < 0)
                AttackText.text = string.Format("{0}<color=red>{1:+0;-#}</color>", baseDamage, damageMod);
            else
                AttackText.text = string.Format("{0}", baseDamage);

            if (!weaponName.Equals(_weaponName))
                UpdateIcon(weaponName);

            _weaponName = weaponName;
        }

        private void UpdateIcon(string weaponName)
        {
            var wi = Appearance.GetForDbKey(weaponName);
            if (wi != null)
                Icon.sprite = wi.Icon;
            else
            {
                Debug.LogWarningFormat("Can't find icon for weapon: {0}", weaponName);
            }
        }
    }
}
