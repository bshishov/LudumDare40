using System;
using System.Linq;
using UnityEngine;

namespace Assets.Scripts.Data
{
    [CreateAssetMenu(menuName = "Appearance/Buffs", fileName = "Buffs")]
    public class BuffAppearance : ScriptableObject
    {
        [Serializable]
        public class BuffInfo
        {
            public string DatabaseKey;
            public Sprite Icon;
        }

        public Sprite DefaultIcon;
        public BuffInfo[] Buffs;

        public Sprite GetIcon(string dbKey)
        {
            var bi = Buffs.FirstOrDefault(b => b.DatabaseKey.Equals(dbKey));
            if (bi != null && bi.Icon != null)
                return bi.Icon;

            return DefaultIcon;
        }
    }
}
