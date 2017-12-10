using System;
using Assets.Scripts.Network;
using Assets.Scripts.Utils;
using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    public class UIEventLog : Singleton<UIEventLog>
    {
        public GameObject MessagePrefab;
        
        void Start ()
        {
            Client.Instance.Subscribe(Protocol.MsgSrvGameEffect, EffectHandler);
            Client.Instance.Subscribe(Protocol.MsgSrvError, ErrorHandler);
            Client.Instance.Subscribe(Protocol.MsgSrvGameTurn, TurnHandler);
        }

        private void EffectHandler(Message message)
        {
            var effect = message.Body["effect"].Value;
            var argument0 = message.Body["args"][0].Value;
            var argument1 = message.Body["args"][1].Value;
            Show(string.Format("Effect <color=yellow>{0}</color> {1} {2}", effect, argument0, argument1));
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
