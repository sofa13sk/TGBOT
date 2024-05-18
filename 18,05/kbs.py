from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
kb_1 = InlineKeyboardMarkup(row_width=1)
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b_1 = InlineKeyboardButton(text="ПОЛУЧИТЬ МОЙ ТГ", url="https://web.telegram.org/a/#5281490334")

b_2 = InlineKeyboardButton(text="ПОЛУЧИТЬ МОЙ ВК", url="https://vk.com/id141073311")
b3 = InlineKeyboardButton(text="По какому вопросу?", callback_data="help 1")
# @advokat_Krivachev
kb_1.add(b_1, b_2, b3)

help_b = KeyboardButton("Гражданское право")
help_b1 = KeyboardButton("Развод и раздел имущества")
help_b2 = KeyboardButton("Уголовное право")

menu_kb.add(help_b,help_b1, help_b2)

kb_2 = InlineKeyboardMarkup(row_width=1)
b_4 = InlineKeyboardButton(text="НЕТ", callback_data="tyhuj3")
b_5 = InlineKeyboardButton(text="ДА", callback_data="13")
kb_2.add(b_4, b_5)

kb_calendar = InlineKeyboardMarkup(row_width=7)

calendar_1 = [InlineKeyboardButton(text="3 июня", callback_data="3u"),
InlineKeyboardButton(text="4 июня", callback_data="4u"),
InlineKeyboardButton(text="5 июня", callback_data="5u"),
InlineKeyboardButton(text="6 июня", callback_data="6u"),
InlineKeyboardButton(text="7 июня", callback_data="7u"),
InlineKeyboardButton(text="10 июня", callback_data="10u"),
InlineKeyboardButton(text="11 июня", callback_data="11u"),
InlineKeyboardButton(text="12 июня", callback_data="12u"),
InlineKeyboardButton(text="13 июня", callback_data="13u"),
InlineKeyboardButton(text="14 июня", callback_data="14u")]




kb_calendar.add(*calendar_1)

kb_calendar_7June = InlineKeyboardMarkup(row_width=3)
calendar_7June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15"),
InlineKeyboardButton(text="15:00 - 16:00", callback_data="15-16"),
InlineKeyboardButton(text="16:00 - 17:00", callback_data="16-17"),
InlineKeyboardButton(text="17:00 - 18:00", callback_data="17-18"),
InlineKeyboardButton(text="18:00 - 19:00", callback_data="18-19"),
InlineKeyboardButton(text="19:00 - 20:00", callback_data="19-20")]

kb_calendar_7June.add(*calendar_7June)

kb_calendar_5June = InlineKeyboardMarkup(row_width=3)
calendar_5June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15"),
InlineKeyboardButton(text="15:00 - 16:00", callback_data="15-16"),
InlineKeyboardButton(text="16:00 - 17:00", callback_data="16-17")]
kb_calendar_5June.add(*calendar_5June)

kb_calendar_6June = InlineKeyboardMarkup(row_width=3)
calendar_6June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15"),
InlineKeyboardButton(text="15:00 - 16:00", callback_data="15-16"),]
kb_calendar_6June.add(*calendar_6June)

kb_calendar_4June = InlineKeyboardMarkup(row_width=3)
calendar_4June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15")]
kb_calendar_4June.add(*calendar_4June)

kb_calendar_10June = InlineKeyboardMarkup(row_width=3)
calendar_10June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15"),
InlineKeyboardButton(text="15:00 - 16:00", callback_data="15-16"),
InlineKeyboardButton(text="16:00 - 17:00", callback_data="16-17")]
kb_calendar_10June.add(*calendar_10June)


kb_calendar_11June = InlineKeyboardMarkup(row_width=3)
calendar_11June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15"),
InlineKeyboardButton(text="15:00 - 16:00", callback_data="15-16"),
InlineKeyboardButton(text="16:00 - 17:00", callback_data="16-17"),
InlineKeyboardButton(text="17:00 - 18:00", callback_data="17-18"),
InlineKeyboardButton(text="18:00 - 19:00", callback_data="18-19"),
InlineKeyboardButton(text="19:00 - 20:00", callback_data="19-20")]
kb_calendar_11June.add(*calendar_11June)

kb_calendar_12June = InlineKeyboardMarkup(row_width=3)
calendar_12June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15"),
InlineKeyboardButton(text="15:00 - 16:00", callback_data="15-16"),
InlineKeyboardButton(text="16:00 - 17:00", callback_data="16-17")]
kb_calendar_12June.add(*calendar_12June)

kb_calendar_13June = InlineKeyboardMarkup(row_width=3)
calendar_13June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15")]
kb_calendar_13June.add(*calendar_13June)

kb_calendar_14June = InlineKeyboardMarkup(row_width=3)
calendar_14June = [InlineKeyboardButton(text="12:00 - 13:00", callback_data="12-13"),
InlineKeyboardButton(text="13:00 - 14:00", callback_data="13-14"),
InlineKeyboardButton(text="14:00 - 15:00", callback_data="14-15"),
InlineKeyboardButton(text="15:00 - 16:00", callback_data="15-16"),
InlineKeyboardButton(text="16:00 - 17:00", callback_data="16-17"),
InlineKeyboardButton(text="17:00 - 18:00", callback_data="17-18"),
InlineKeyboardButton(text="18:00 - 19:00", callback_data="18-19"),
InlineKeyboardButton(text="19:00 - 20:00", callback_data="19-20")]
kb_calendar_14June.add(*calendar_14June)