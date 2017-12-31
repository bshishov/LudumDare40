using Assets.Scripts.Utils;
using Protocol;
using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    public class UIEventLog : Singleton<UIEventLog>
    {
        public GameObject MessagePrefab;
        
        void Start ()
        {
            Client.Instance.Subscribe(Head.SrvGameEffect, EffectHandler);
            Client.Instance.Subscribe(Head.SrvError, ErrorHandler);
            Client.Instance.Subscribe(Head.SrvGameTurn, TurnHandler);
        }

        private void EffectHandler(Message message)
        {
            var effect = message.Game.Effect;
            //var argument0 = message.Body["args"][0].Value;
            //var argument1 = message.Body["args"][1].Value;
            //Show(string.Format("Effect <color=yellow>{0}</color> {1} {2}", effect, argument0, argument1));
            Show(string.Format("Effect <color=yellow>{0}</color>", effect));
        }

        private void ErrorHandler(Message message)
        {
            Show(string.Format("<color=red>{0}</color>", message.Status));
        }

        private void TurnHandler(Message message)
        {
            Show(string.Format("<color=green>New turn</color>"));
        }

        public void Show(string message)
        {
            if (MessagePrefab != null)
            {
                var go = (GameObject) GameObject.Instantiate(MessagePrefab, transform);
                var text = go.GetComponent<Text>();
                if (text != null)
                { 
                    text.text = message;
                }
            }
        }
    }
}
