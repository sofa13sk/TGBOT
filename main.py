from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_BOT
from kbs import kb_1, menu_kb, kb_calendar
from text import HELP

bot = Bot(token=TOKEN_BOT)
dp =Dispatcher(bot)

@dp.message_handler(commands=["start", "старт"])
async def start_cmd(msg: types.Message):
    await msg.answer(text="Добро пожаловать!", reply_markup=kb_1)




@dp.message_handler(text="Гражданское право")
async def help_cmd(msg: types.Message):
    await msg.answer(text="Услышили вас, когда вам будет удобно придти?")
    await bot.send_message(chat_id=1234, text=)


@dp.callback_query_handler(text="help 1")
async def help_cmd(call: types.CallbackQuery):
    await call.message.answer(text=HELP, reply_markup=menu_kb)
    await call.answer()

@dp.callback_query_handler(text="1m")
async def may_1(call: types.CallbackQuery):
    await call.message.answer()

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)