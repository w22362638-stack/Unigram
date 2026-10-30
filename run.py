api_id = رقمك_هنا
api_hash = "هاشك_هنا"
api_id = 1234567        # الرقم اللي طلع لك، بدون علامات اقتباس
api_hash = "abcdef..."  # الهاش بين علامات اقتباس
from telethon import TelegramClient, events

api_id = 12345678
api_hash = "ضع_الهاش_هنا"

client = TelegramClient("session", api_id, api_hash)

replies = {
    "t.me": "شكراً على الرابط ✅",
    "سلام": "وعليكم السلام",
    "السعر": "السعر على الخاص",
}

@client.on(events.NewMessage(chats=[-1001234567890]))
async def handler(event):
    if event.out:
        return
    text = event.raw_text or ""
    for key, answer in replies.items():
        if key in text:
            await event.reply(answer)
            break

client.start()
client.run_until_disconnected()

