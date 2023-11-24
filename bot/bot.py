from telethon.sync import TelegramClient, events
import logging as log

accept_list_users: list[int] = []


async def start_bot(api_id: int, api_hash: str, version: str, phone_number: str, logging: log):
    # with TelegramClient("session", api_id, api_hash) as client:
    #    client.send_message("me", f"Bot started\nversion: {version}")

    #    @client.on(events.NewMessage(pattern="*"))
    #    async def is_user_true(event):
    #        # print(event)
    #        # client.get_messages
    #        await event.reply('Hey!')
    client = TelegramClient('session', api_id, api_hash)
    assert await client.connect()
    if not client.is_user_authorized():
        await client.send_code_request(phone_number)
        me = await client.sign_in(phone_number, input('Enter code: '))
        print(me)

    await client.send_message("me", f"Bot started\nversion: {version}")

    @client.on(events.NewMessage(pattern="*"))
    async def is_user_true(event):
        # print(event)
        # client.get_messages
        await event.reply('Hey!')
