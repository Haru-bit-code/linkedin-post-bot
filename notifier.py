import asyncio
from telegram import Bot
import config

async def send_telegram(message):
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)          
    await bot.send_message(
        chat_id=config.TELEGRAM_CHAT_ID,             
        text=message                  
    )

def send_message(message):       
    asyncio.run(send_telegram(message))              