import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage




from protection import check_user, temporarily_stop
from bd import add_or_update_user, initialize_database
from config import API_TOKEN
from record_log import log_error, log_info





log_info('бот запущен')


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


router = Router()

initialize_database()





@router.message(Command('start'))
async def index(message: types.Message):
    ID = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username



    if check_user(ID):
        return




    add_or_update_user(ID, name, username)



    try:
        await message.answer(
            text=(
                f"👋 Hi! 👋\n\n"
                f"🆔 Your unique ID: `{ID}`\n\n"
                f"🤖 This bot is simple: it only sends your ID when you start it.\n\n"
                f"🔒 Spam protection is enabled!\n"
                f"I respond once every 1 minutes to avoid abuse.\n\n"
                f"💻 The bot is open source!\n"
                f"You can view and contribute to the code on GitHub [here](https://github.com/paulilich/GetMyID-Bot)\n\n"
                f"😊 Thanks for understanding!"
            ),
            parse_mode='Markdown',
            disable_web_page_preview=True

        )

    except Exception as e:
        log_error(f'Ошибка при отправке сообщения юзеру: {ID}\n{e}')



    temporarily_stop(ID)




@dp.message(F.content_type == types.ContentType.STICKER)
async def handle_sticker(message: types.Message):
    ID = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username

    sticker_id = message.sticker.file_id



    if check_user(ID):
        return


    add_or_update_user(ID, name, username)


    try:
        await message.answer(
            text=(
                f"😊 *Thanks for the sticker!* 😊\n\n"
                f"🆔 *Your unique ID:* `{ID}`\n\n"
                f"📌 *Sticker ID:* `{sticker_id}`\n\n"
                f"🤖 *I don’t know how to react to it yet, but I’ll learn soon!*"
            ),
            parse_mode="Markdown"
        )

    except Exception as e:
        log_error(f'Ошибка при отправке сообщения юзеру: {ID}\n{e}')


    temporarily_stop(ID)







async def main():
    dp.include_router(router)



    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())
