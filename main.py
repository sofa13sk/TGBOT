from aiogram import Bot, Dispatcher, executor, types
from confik import TOKEN_BOT
from kb import kb_1
import random
bot = Bot(token=TOKEN_BOT)
dp =Dispatcher(bot)

@dp.message_handler(commands=["start", "старт"])
async def start_cmd(msg: types.Message):
    await msg.answer(text="Добро пожаловать!", reply_markup=kb_1)


@dp.callback_query_handler(text="☻")
async def random_num(call: types.CallbackQuery):
    num = random.randint(1, 10)
    await call.message.answer(text=f"ТЫ получил число: {num}")
    await call.answer(text="Спасибо и удачи!")

@dp.callback_query_handler(text="fgh")
async def hello(call: types.CallbackQuery):
    await call.message.answer(text="я еще ничего не придумала", reply_markup=)
    await call.message.answer(text="Пока-пока")
    await call.answer()

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)