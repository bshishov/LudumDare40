using System;
using System.Net.Sockets;

namespace Assets.Scripts.Network
{
    public interface IMessageSerializer<T>
    {
        byte[] Serialize(T message);
        T Deserialize(ArraySegment<byte> data);
    }

    public class NetworkChannel<T> : IDisposable
    {
        public const int BufferSize = 8192;

        public event Action<NetworkChannel<T>> Connected;
        public event Action<NetworkChannel<T>, T> Received;
        public event Action<NetworkChannel<T>, Exception> ErrorOccured;

        public bool IsConnected {
            get { return _tcpClient != null && _tcpClient.Connected && _tcpStream != null; }
        }

        private TcpClient _tcpClient;
        private NetworkStream _tcpStream;
        private readonly IMessageSerializer<T> _serializer;
        private readonly PacketReader _reader;

        public NetworkChannel(IMessageSerializer<T> serializer)
        {
            _serializer = serializer;
            _reader = new PacketReader();
        }

        public void Start(string host, int port)
        {
            _tcpClient = new TcpClient();
            _tcpClient.BeginConnect(host, port, new AsyncCallback(OnConnect), _tcpClient);
        }

        public void Send(T message)
        {
            if (_tcpClient != null && _tcpClient.Connected && _tcpStream != null)
            {
                var msgBuff = _serializer.Serialize(message);
                var msgLen = (short)msgBuff.Length;

                var buff = new byte[2 + msgBuff.Length];
                System.Buffer.BlockCopy(BitConverter.GetBytes(msgLen), 0, buff, 0, 2);
                System.Buffer.BlockCopy(msgBuff, 0, buff, 2, msgBuff.Length);
                _tcpStream.BeginWrite(buff, 0, buff.Length, (ar) =>
                {
                    try
                    {
                        _tcpStream.EndWrite(ar);
                    }
                    catch (Exception ex)
                    {
                        if (ErrorOccured != null)
                            ErrorOccured.Invoke(this, ex);
                    }
                }, null);
            }
        }

        private void OnConnect(IAsyncResult ar)
        {
            try
            {
                // Retrieve the socket from the state object.  
                var client = (TcpClient)ar.AsyncState;

                // Complete the connection.  
                client.EndConnect(ar);

                _tcpStream = _tcpClient.GetStream();

                if(Connected != null)
                    Connected.Invoke(this);
                
                _reader.StartReceiving(_tcpStream, Process);
            }
            catch (Exception ex)
            {
                if (ErrorOccured != null)
                    ErrorOccured.Invoke(this, ex);
            }
        }

        private void Process(ArraySegment<byte> arraySegment)
        {
            var msg = _serializer.Deserialize(arraySegment);
            
            if (Received != null)
                Received.Invoke(this, msg);
        }

        public void Close()
        {
            if (_tcpStream != null)
                _tcpStream.Close();
            if (_tcpClient != null)
                _tcpClient.Close();
        }

        public void Dispose()
        {
            Close();
            if (_tcpClient != null) ((IDisposable) _tcpClient).Dispose();
            if (_tcpStream != null) _tcpStream.Dispose();
        }
    }
}
