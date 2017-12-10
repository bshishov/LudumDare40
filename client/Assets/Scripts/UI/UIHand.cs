using System;
using System.Collections.Generic;
using SimpleJSON;
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

        private void OnStateUpdated(JSONObject gameState)
        {
            var state = BattleManager.Instance.StateForPerspective(Perspective);
            if (state == null)
                return;

            foreach (var uiCard in _cards)
                Destroy(uiCard.gameObject);

            _cards.Clear();

            var hand = state[Rules.PStateHand];
            foreach (var cardState in hand.Children)
            {
                AddCard(cardState.AsObject);
            }
        }

        private void AddCard(JSONObject cardState)
        {
            var go = (GameObject)GameObject.Instantiate(CardPrefab, transform);
            var uicard = go.GetComponent<UICard>();
            uicard.UpdateState(cardState, BattleManager.Instance.IsOffense(Perspective));
            _cards.Add(uicard);
        }
    }
}
