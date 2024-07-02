import warnings
import asyncio
from telegram import Bot


warnings.filterwarnings("ignore", category=DeprecationWarning)

bot_token = '7320016249:AAH9wV_QttEVNnzlWw5wiqIvjWNgC1TQ4ow'
bot = Bot(token=bot_token)


chat_id = '-4275778465'


async def main(message):
    try:

        await bot.send_message(chat_id=chat_id, text=message)
        return 'Message sent successfully!'
    except Exception as e:
        return 'Failed to send message no money :sad: '

def send(message):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(message))

    
    

