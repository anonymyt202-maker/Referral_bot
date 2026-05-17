import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from data.config import BOT_TOKEN

from handlers.users.start import router as start_router
from handlers.users.menu import router as menu_router
from handlers.admins.admin import router as admin_router


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


async def main():

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(admin_router)

    print("Bot ishga tushdi ✅")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
