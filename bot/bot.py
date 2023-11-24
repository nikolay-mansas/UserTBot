from telethon.sync import TelegramClient, events
import logging as log

accept_list_users: list[int] = []


async def start_bot(api_id: int, api_hash: str, version: str, logging: log):
    with TelegramClient("session", api_id, api_hash) as client:
        client.send_message("me", f"Bot started\nversion: {version}")

        @client.on(events.NewMessage(pattern="*"))
        async def is_user_true(event):
            # print(event)
            # client.get_messages
            await event.reply('Hey!')
