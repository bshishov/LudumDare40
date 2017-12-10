using System.Collections.Generic;
using Assets.Scripts.Network;
using Assets.Scripts.Utils;
using UnityEngine;

namespace Assets.Scripts.UI
{
    public class LobbyUIManager : Singleton<LobbyUIManager>
    {
        private string _selectedWeapon;
        private string _selectedShip;

        private IEnumerable<UIWeaponIcon> _weaponIcons;
        private IEnumerable<UIShipIcon> _shipIcons;

        void Start ()
        {
            _weaponIcons = GameObject.FindObjectsOfType<UIWeaponIcon>();
            _shipIcons = GameObject.FindObjectsOfType<UIShipIcon>();
        }
        
        void Update ()
        {
		
        }

        public void SelectWeapon(string weaponName)
        {
            _selectedWeapon = weaponName;
            Debug.LogFormat("WeaponInfo selected: {0}", _selectedWeapon);

            foreach (var weaponIcon in _weaponIcons)
                weaponIcon.SetSelected(weaponIcon.WeaponName.Equals(_selectedWeapon));
        }

        public void SelectShip(string shipName)
        {
            _selectedShip = shipName;
            Debug.LogFormat("Ship selected: {0}", _selectedShip);

            foreach (var shipIcon in _shipIcons)
                shipIcon.SetSelected(shipIcon.ShipName.Equals(_selectedShip));
        }

        public void StartQueue()
        {
            if(string.IsNullOrEmpty(_selectedShip))
                return;

            if (string.IsNullOrEmpty(_selectedWeapon))
                return;

            foreach (var weaponIcon in _weaponIcons)
                weaponIcon.SetInteractible(false);

            foreach (var shipIcon in _shipIcons)
                shipIcon.SetInteractible(false);

            Debug.Log("Starting queue");
            Client.Instance.StartQueue(_selectedShip, _selectedWeapon);
        }

        public void StopQueue()
        {
            foreach (var weaponIcon in _weaponIcons)
                weaponIcon.SetInteractible(true);

            foreach (var shipIcon in _shipIcons)
                shipIcon.SetInteractible(true);
        }
    }
}
