from pyrogram import *
import requests
import os


API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

aqua = Client(
    "my_bot",
    bot_token= BOT_TOKEN,
    api_id= API_ID,
    api_hash= API_HASH
    
)



@aqua.on_message(filters.command(["start"]))
async def start (client , message):
    await message.reply_text(text = ''' I AM KANNA-CHAN ✨ 
    \n\n I AM YOUR VIRTUAL FRIEND ✨
    \n\nI CAN REPLY TO ANY TEXT MESSAGE YOU SEND✨''')

@aqua.on_message()
async def kuki (client , message):
    msg = message.text
    r = requests.get(url = f"https://www.kuki-api.tk/api/message={msg} " )
    print(f"https://www.kuki-api.tk/api/message={msg}")
    data = r.json()
    print(data)
    await message.reply_text(data['reply'])

@aqua.on_message(filters.command(["help"]))
async def support (client , message):
    await message.reply_text('join : @fossaf *blushes*')



aqua.run()



