from pyrogram import Client

from .config import Config
from .database import Database


class ScreenShotBot(Client):

    def __init__(self):
        super().__init__(
            session_name=Config.SESSION_NAME,
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            workers = 20,
            plugins = dict(
                root="bot/plugins"
            )
        )

        self.db = Database(Config.DATABASE_URL, Config.SESSION_NAME)
        self.CURRENT_PROCESSES = {}
        self.CHAT_FLOOD = {}
        self.broadcast_ids = {}


    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"\n\nNew session started for {me.first_name}({me.username})")


    async def stop(self):
        await super().stop()
        print('Session stopped. Bye!!')
