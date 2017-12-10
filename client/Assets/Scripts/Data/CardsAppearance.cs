using System;
using System.Linq;
using UnityEngine;

namespace Assets.Scripts.Data
{
    [CreateAssetMenu(menuName = "Appearance/Cards", fileName = "Cards")]
    public class CardsAppearance : ScriptableObject
    {
        [Serializable]
        public class TypeColorMapping
        {
            public string Type;
            public Color Color;
        }

        public Color DefaultColor;
        public Sprite OffenseIcon;
        public Sprite DefenseIcon;
        public TypeColorMapping[] Mappings;

        public Color GetColorForType(string type)
        {
            var tcm = Mappings.FirstOrDefault(m => m.Type.Equals(type));
            if (tcm != null)
                return tcm.Color;
            return DefaultColor;
        }
    }
}
