using System;
using SimpleJSON;
using UnityEngine;

namespace Assets.Scripts.Network
{
    public class Message
    {
        public string Domain { get; set; }
    
        public string Head { get; set; }
    
        public string Status { get; set; }
    
        public JSONNode Body { get; set; }

        public Message(string domain, string head, string status = "")
        {
            Domain = domain;
            Head = head;
            Status = status;
            Body = new JSONObject();
        }

        public Message(string data)
        {
            Parse(data);
        }

        public void Parse(string data)
        {
            try
            {
                var node = JSON.Parse(data);
                Domain = node[Protocol.KeyDomain];
                Head = node[Protocol.KeyHead];
                Status = node[Protocol.KeyStatus];
                Body = node[Protocol.KeyBody];
            }
            catch (Exception ex)
            {
                Debug.LogWarningFormat("Failed to parse incomng message: {0}, {1}", data, ex);
            }
        }

        public bool DomainIs(string domain)
        {
            return Domain.Equals(domain, StringComparison.InvariantCultureIgnoreCase);
        }

        public bool Is(string head)
        {
            return Head.Equals(head, StringComparison.InvariantCultureIgnoreCase);
        }

        public override string ToString()
        {
            var o = new JSONObject();
            o[Protocol.KeyDomain] = Domain;
            o[Protocol.KeyHead] = Head;
            o[Protocol.KeyStatus] = Status;
            o[Protocol.KeyBody] = Body;
            return o.ToString();
        }
    }
}