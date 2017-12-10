using System;
using System.Linq;
using UnityEngine;

namespace Assets.Scripts.Data
{
    [CreateAssetMenu(menuName = "Appearance/Weapons", fileName = "Weapons")]
    public class WeaponsAppearance : ScriptableObject
    {
        public WeaponInfo[] Weapons;

        public WeaponInfo GetForDbKey(string key)
        {
            return Weapons.FirstOrDefault(weapon => weapon.DatabaseKey.Equals(key, StringComparison.InvariantCultureIgnoreCase));
        }
    }
}
