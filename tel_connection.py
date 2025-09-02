import asyncio
from telethon import TelegramClient, events
from database import get_db


api_id = int(input("Telegram Api id kiriting: "))
api_hash = input("Telegram Api Hash kiriting: ")
phone_number = input("Telefon raqam: misol (+998123456789) ")

async def main():
    # Client ochamiz
    async with TelegramClient('session_name', api_id, api_hash) as client:

        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            code = input('Kod kiriting: ')
            await client.sign_in(phone_number, code)

        group_username = input("Guruh username yoki link kiriting (masalan: @pythonuz yoki https://t.me/+abc123): ")
        group_entity = await client.get_entity(group_username)

        @client.on(events.NewMessage(chats=group_entity))
        async def handler(event):
            sender = await event.get_sender()
            sender_name = getattr(sender, 'first_name', 'Noma’lum')
            print(f"[{sender_name}] -> {event.message.text}")

        print(f"Guruhdagi xabarlar tinglanmoqda: {group_entity.title}")
        await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
