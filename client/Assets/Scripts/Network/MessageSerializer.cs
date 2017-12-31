using System;
using System.Text;
using Google.Protobuf;
using Protocol;

namespace Assets.Scripts.Network
{
    public class MessageSerializer : IMessageSerializer<Message>
    {
        public byte[] Serialize(Message message)
        {
            return message.ToByteArray();
        }

        public Message Deserialize(ArraySegment<byte> data)
        {
            if (data.Array == null)
                return null;

            var msgBuffer = new byte[data.Count];
            Array.Copy(data.Array, data.Offset, msgBuffer, 0, data.Count);

            var message = new Message();
            message.MergeFrom(msgBuffer);
            return message;
        }
    }
}