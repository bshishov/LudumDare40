using SimpleJSON;
using System;
using UnityEngine;

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
            Domain = node["domain"];
            Head = node["head"];
            Status = node["status"];
            Body = node["body"];
            Debug.LogFormat("Parsed: {0}", node.ToString());
        }
        catch (Exception e)
        {
            Debug.LogWarningFormat("Failed to parse incomng message: {0}", data);
            return;
        }
    }

    public override string ToString()
    {
        var o = new JSONObject();
        o["domain"] = Domain;
        o["head"] = Head;
        o["status"] = Status;
        o["body"] = Body;
        return o.ToString();
    }
}