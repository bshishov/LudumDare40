using System;
using System.Diagnostics;
using System.Net.Sockets;


namespace Assets.Scripts.Network
{
    public static class NetworkStreamReader
    {
        // This method will continues read until count bytes are read. (or socket is closed)
        private static void DoReadFromSocket(NetworkStream socket, int bytesRead, int count, byte[] buffer, Action<ArraySegment<byte>> endRead)
        {
            // Start a BeginReceive.
            try
            {
                socket.BeginRead(buffer, bytesRead, count - bytesRead, (asyncResult) =>
                {
                    // Get the bytes read.
                    int read = 0;
                    try
                    {
                        // if this goes wrong, the read remains 0
                        read = socket.EndRead(asyncResult);
                    }
                    catch (ObjectDisposedException) { }
                    catch (Exception exception)
                    {
                        Trace.TraceError(exception.Message);
                    }


                    // if zero bytes received, the socket isn't available anymore.
                    if (read == 0)
                    {
                        endRead(new ArraySegment<byte>(buffer, 0, 0));
                        return;
                    }

                    // increase the bytesRead, (position within the buffer)
                    bytesRead += read;

                    // if all bytes are read, call the endRead with the buffer.
                    if (bytesRead == count)
                        // All bytes are read. Invoke callback.
                        endRead(new ArraySegment<byte>(buffer, 0, count));
                    else
                        // if not all bytes received, start another BeginReceive.
                        DoReadFromSocket(socket, bytesRead, count, buffer, endRead);

                }, null);
            }
            catch (Exception exception)
            {
                Trace.TraceError(exception.Message);
                endRead(new ArraySegment<byte>(buffer, 0, 0));
            }
        }

        public static void ReadFromNetworkStream(NetworkStream socket, int count, Action<ArraySegment<byte>> endRead)
        {
            // read from socket, construct a new buffer.
            DoReadFromSocket(socket, 0, count, new byte[count], endRead);
        }

        public static void ReadFromNetworkStream(NetworkStream socket, int count, byte[] buffer, Action<ArraySegment<byte>> endRead)
        {
            // if you do have a buffer available, you can pass that one. (this way you do not construct new buffers for receiving and able to reuse buffers)

            // if the buffer is too small, raise an exception, the caller should check the count and size of the buffer.
            if (count > buffer.Length)
                throw new ArgumentOutOfRangeException("count");

            DoReadFromSocket(socket, 0, count, buffer, endRead);
        }
    }

    public class PacketReader
    {
        private byte[] _receiveBuffer = new byte[2];

        // This will run until the socket is closed.    
        public void StartReceiving(NetworkStream socket, Action<ArraySegment<byte>> process)
        {
            NetworkStreamReader.ReadFromNetworkStream(socket, 2, _receiveBuffer, (headerData) =>
            {
                if (headerData.Count == 0)
                {
                    // nothing/closed
                    return;
                }

                // Read the length of the data.
                int length = BitConverter.ToInt16(headerData.Array, headerData.Offset);

                // if the receive buffer is too small, reallocate it.
                if (_receiveBuffer.Length < length)
                    _receiveBuffer = new byte[length];

                NetworkStreamReader.ReadFromNetworkStream(socket, length, _receiveBuffer, (dataBufferSegment) =>
                {
                    if (dataBufferSegment.Count == 0)
                    {
                        // nothing/closed
                        return;
                    }

                    try
                    {
                        process(dataBufferSegment);
                    }
                    catch { }

                    StartReceiving(socket, process);
                });
            });
        }
    }
}
