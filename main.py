import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession

from handlers import router

session = AiohttpSession(proxy='http://proxy.server:3128/')

# before putting it into server I need to add session into bot
bot = Bot(token='7238224907:AAFeBfVkKruDuljIYv6JJV7BpDNDEnpHJNY', session=session, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

#
# async def start_up(bot: Bot):
#     await bot.send_message(chat_id=1454665869, text='Bot ishga tushdi.')


async def main():
    dp.include_router(router)
    # dp.startup.register(start_up)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, polling_timeout=1)
    
    # Do not know does it work or no
    # await dp.start_polling(bot, skip_updates=False, polling_timeout=1)


if __name__ == '__main__':
    try:
        print('Success')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')