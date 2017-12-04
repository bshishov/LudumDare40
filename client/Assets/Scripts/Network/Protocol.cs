namespace Assets.Scripts.Network
{
    class Protocol
    {
        /// <summary>
        /// These values must be exact as server
        /// </summary>

        public const string MsgDomainGame = "game";
        public const string MsgDomainLobby = "lobby";

        public const string MsgDefault = "";

        // [SERVER] Base server messages
        public const string MsgSrvError = "s.error";

        public const string MsgSrvHello = "s.hello";

        // [SERVER] Queue message
        public const string MsgSrvQueueStarted = "s.q.started";

        public const string MsgSrvQueueStopped = "s.q.stopped";
        public const string MsgSrvQueueGameCreated = "s.g.created";

        // [SERVER] Game messages
        public const string MsgSrvGameBegin = "s.g.begin";

        public const string MsgSrvGameEnd = "s.g.end";
        public const string MsgSrvGamePlayerLeft = "s.g.player_left";
        public const string MsgSrvGameTurn = "s.g.turn";
        public const string MsgSrvGameAction = "s.g.action"; // redirect player action
        public const string MsgSrvGameEffect = "s.g.effect";

        // [CLIENT] Messages
        public const string MsgCliQueueStart = "c.q.start";

        public const string MsgCliQueueStop = "c.q.stop";
        public const string MsgCliGameAction = "c.g.action";

        public static byte[] MessageSeparator = new byte[] { 0x00, 0x01, 0x00, 0x01, 0x00, 0x01 };


        public const string KeyDomain = "domain";
        public const string KeyHead = "head";
        public const string KeyBody = "body";
        public const string KeyStatus = "status";

        public const string KeyShip = "ship";
        public const string KeyWeapon = "weapon";
        public const string KeyGameId = "game_id";
        public const string KeySide= "side";
    }
}