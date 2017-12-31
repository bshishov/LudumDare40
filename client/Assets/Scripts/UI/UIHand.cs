using System;
using System.Collections.Generic;
using Assets.Scripts.Data;
using Protocol;
using UnityEngine;

namespace Assets.Scripts.UI
{
    public class UIHand : MonoBehaviour
    {
        public GameObject CardPrefab;
        public Perspective Perspective = Perspective.My;

        private readonly List<UICard> _cards = new List<UICard>();

        void Start ()
        {
		    BattleManager.Instance.StateUpdated += OnStateUpdated;
        }

        private void OnStateUpdated(GameState gameState)
        {
            var state = BattleManager.Instance.PlayerEntityState(Perspective);
            if (state == null)
                return;

            foreach (var uiCard in _cards)
                Destroy(uiCard.gameObject);

            _cards.Clear();
            
            foreach (var cardState in state.Hand)
            {
                AddCard(cardState);
            }
        }

        private void AddCard(CardState cardState)
        {
            var go = (GameObject)GameObject.Instantiate(CardPrefab, transform);
            var uicard = go.GetComponent<UICard>();
            uicard.UpdateState(cardState, BattleManager.Instance.IsOffense(Perspective));
            _cards.Add(uicard);
        }
    }
}
