using System;
using System.Text;

namespace Assets.Scripts.Network
{
    public class MessageSerializer : IMessageSerializer<Message>
    {
        public byte[] Serialize(Message message)
        {
            return Encoding.UTF8.GetBytes(message.ToString());
        }

        public Message Deserialize(ArraySegment<byte> data)
        {
            var str = Encoding.UTF8.GetString(data.Array, data.Offset, data.Count);
            return new Message(str);
        }
    }
}