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
           
            UpdateAttack(damageMod);

            if (!weaponName.Equals(_weaponName))
            {
                UpdateIcon(weaponName);
                // TODO: update tooltip
            }

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

        private void UpdateAttack(int attackModifier)
        {
            AttackText.text = attackModifier.ToString("+0;-#");
        }
    }
}
