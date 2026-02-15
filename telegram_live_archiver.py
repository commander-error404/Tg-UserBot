import os
import asyncio
from datetime import datetime
from telethon import TelegramClient, events

api_id = 12345678
api_hash = "0123456789abcdef0123456789abcdef"

CHANNEL = "channelusername"  # without @
MERGE_WINDOW = 15  # seconds


BASE_DIR = "archive"
os.makedirs(BASE_DIR, exist_ok=True)

client = TelegramClient("session", api_id, api_hash)

buffer = []
last_message_time = None

async def flush_buffer():
    global buffer

    if not buffer:
        return

    timestamp = buffer[0]["time"].strftime("%Y-%m-%d_%H-%M-%S")
    folder = os.path.join(BASE_DIR, timestamp)
    os.makedirs(folder, exist_ok=True)

    texts = []

    for i, msg in enumerate(buffer):
        if msg["message"].text:
            texts.append(msg["message"].text)

        if msg["message"].media:
            await client.download_media(
                msg["message"],
                file=os.path.join(folder, f"{i+1}")
            )

    with open(os.path.join(folder, "text.txt"), "w", encoding="utf-8") as f:
        f.write("\n\n".join(texts))

    print(f"💾 Post saved: {folder}")

    buffer.clear()

@client.on(events.NewMessage(chats=CHANNEL))
async def handler(event):
    global buffer, last_message_time

    now = datetime.utcnow()

    if last_message_time and (now - last_message_time).seconds > MERGE_WINDOW:
        await flush_buffer()

    last_message_time = now

    buffer.append({
        "time": now,
        "message": event.message
    })

    await asyncio.sleep(MERGE_WINDOW)

    if buffer and (datetime.utcnow() - last_message_time).seconds >= MERGE_WINDOW:
        await flush_buffer()

async def main():
    print("📡Connection ...")
    await client.start()
    print("✅ listening the channel:", CHANNEL)
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
