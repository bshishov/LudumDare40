using Assets.Scripts.Network;
using UnityEngine;
using UnityEngine.UI;

namespace Assets.Scripts.UI
{
    [RequireComponent(typeof(Button))]
    public class UIFindGameButton : MonoBehaviour
    {
        public string SearchingText = "Searching...";
        public string IdleText = "Find Game";
        public string CreatedText = "Game Found!";

        private Button _button;
        private Text _text;
        
        void Start ()
        {
            _button = GetComponent<Button>();
            _text = GetComponentInChildren<Text>();
            _button.onClick.AddListener(() =>
            {
                LobbyUIManager.Instance.StartQueue();
            });
            
            Client.Instance.Subscribe(Protocol.MsgSrvQueueStarted, message =>
            {
                _text.text = SearchingText;
                _button.interactable = false;
            });

            Client.Instance.Subscribe(Protocol.MsgSrvQueueStopped, message =>
            {
                _text.text = IdleText;
                _button.interactable = true;
            });

            Client.Instance.Subscribe(Protocol.MsgSrvQueueGameCreated, message =>
            {
                _text.text = CreatedText;
            });
        }
    }
}
