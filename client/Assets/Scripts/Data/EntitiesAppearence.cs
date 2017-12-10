using System;
using System.Linq;
using UnityEngine;

namespace Assets.Scripts.Data
{
    [CreateAssetMenu(menuName = "Appearance/Entities", fileName = "Entities")]
    public class EntitiesAppearence : ScriptableObject
    {
        public GameObject DefaultPrefab;
        public EntityInfo[] Entities;

        public EntityInfo GetForDbKey(string key)
        {
            return Entities.FirstOrDefault(e => e.DatabaseKey.Equals(key, StringComparison.InvariantCultureIgnoreCase));
        }

        public GameObject GetPrefab(string key)
        {
            var ei = Entities.FirstOrDefault(e => e.DatabaseKey.Equals(key, StringComparison.InvariantCultureIgnoreCase));
            if (ei != null)
                if(ei.Prefab != null)
                    return ei.Prefab;

            return DefaultPrefab;
        }
    }
}
