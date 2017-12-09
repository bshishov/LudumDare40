using System;
using System.Collections.Generic;
using UnityEngine;

namespace Assets.Scripts.Utils
{
    public class ActionDispatcher : MonoBehaviour
    {
        // Dispatching
        private readonly List<System.Action> _dispatchList = new List<Action>();
        private readonly List<System.Action> _dispatchListCopy = new List<Action>();
        private bool _dispatching;
        private readonly object _dispatchLock = new object();

        public void Dispatch(System.Action action)
        {
            lock (_dispatchLock)
            {
                _dispatchList.Add(action);
                _dispatching = true;
            }
        }

        void Update()
        {
            if (!_dispatching)
                return;

            lock (_dispatchLock)
            {
                _dispatchListCopy.AddRange(_dispatchList);
                _dispatchList.Clear();
            }

            foreach (var action in _dispatchListCopy)
            {
                action.Invoke();
            }

            _dispatchListCopy.Clear();
        }
    }
}
