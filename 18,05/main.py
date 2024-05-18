from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_BOT
from kbs import kb_1, menu_kb, kb_calendar, kb_calendar_4June, kb_calendar_5June, kb_calendar_6June, kb_calendar_7June, kb_calendar_10June, kb_calendar_11June, kb_calendar_12June, kb_calendar_13June, kb_calendar_14June, kb_2
from text import HELP, DA

bot = Bot(token=TOKEN_BOT)
dp =Dispatcher(bot)

@dp.message_handler(commands=["start", "старт"])
async def start_cmd(msg: types.Message):
    await msg.answer(text="Добро пожаловать!", reply_markup=kb_1)




@dp.message_handler(text="Гражданское право")
async def help_cmd(msg: types.Message):
    await msg.answer(text="Услышили вас, когда вам будет удобно придти?", reply_markup=kb_calendar)

@dp.message_handler(text="Развод и раздел имущества")
async def help_cmd(msg: types.Message):
    await msg.answer(text="Вы хотите расторгнуть брак?", reply_markup=kb_2)

@dp.callback_query_handler(text="13")
async def help1_cmd(call: types.CallbackQuery):
    await call.message.answer(text="Есть ли у вас дети?", reply_markup=kb_2)
    await call.answer()

@dp.callback_query_handler(text="help 1")
async def help_cmd(call: types.CallbackQuery):
    await call.message.answer(text=HELP, reply_markup=menu_kb)
    await call.answer()

@dp.callback_query_handler(text="4u")
async def June_4(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 4 июня:", reply_markup=kb_calendar_4June)
    await call.answer()

@dp.callback_query_handler(text="12-13")
async def time_4June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_4June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_4June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")



@dp.callback_query_handler(text="5u")
async def June_5(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 5 июня:", reply_markup=kb_calendar_5June)
    await call.answer()
@dp.callback_query_handler(text="12-13")
async def time_5June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_5June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_5June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="15-16")
async def time_5June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")



@dp.callback_query_handler(text="6u")
async def June_6(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 6 июня:", reply_markup=kb_calendar_6June)
    await call.answer()
@dp.callback_query_handler(text="12-13")
async def time_6June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_6June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_6June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="15-16")
async def time_6June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="16-17")
async def time_6June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")



@dp.callback_query_handler(text="7u")
async def June_7(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 7 июня:", reply_markup=kb_calendar_7June)
    await call.answer()
@dp.callback_query_handler(text="12-13")
async def time_7June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_7June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_7June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="15-16")
async def time_7June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="16-17")
async def time_7June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="17-18")
async def time_7June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="18-19")
async def time_7June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="19-20")
async def time_7June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")



@dp.callback_query_handler(text="10u")
async def June_10(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 10 июня:", reply_markup=kb_calendar_10June)
    await call.answer()
@dp.callback_query_handler(text="12-13")
async def time_10June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_10June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_10June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="15-16")
async def time_10June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")


@dp.callback_query_handler(text="11u")
async def June_11(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 11 июня:", reply_markup=kb_calendar_11June)
    await call.answer()
@dp.callback_query_handler(text="12-13")
async def time_11June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_11June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_11June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="15-16")
async def time_11June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="16-17")
async def time_11June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="17-18")
async def time_11June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="18-19")
async def time_11June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="19-20")
async def time_11June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")


@dp.callback_query_handler(text="12u")
async def June_12(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 12 июня:", reply_markup=kb_calendar_12June)
    await call.answer()
@dp.callback_query_handler(text="12-13")
async def time_12June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_12June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_12June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="15-16")
async def time_12June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")


@dp.callback_query_handler(text="13u")
async def June_13(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 13 июня:", reply_markup=kb_calendar_13June)
    await call.answer()

@dp.callback_query_handler(text="12-13")
async def time_13June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_13June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_13June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")


@dp.callback_query_handler(text="14u")
async def June_14(call: types.CallbackQuery):
    await call.message.answer(text="Время приёма на 14 июня:", reply_markup=kb_calendar_14June)
    await call.answer()
@dp.callback_query_handler(text="12-13")
async def time_14June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="13-14")
async def time_14June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="14-15")
async def time_14June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="15-16")
async def time_14June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="16-17")
async def time_14June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="17-18")
async def time_14June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="18-19")
async def time_14June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")

@dp.callback_query_handler(text="19-20")
async def time_14June(call: types.CallbackQuery):
    await call.answer(text="Вы успешно записались, до встречи!")






if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
