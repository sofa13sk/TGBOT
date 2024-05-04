from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
kb_1 = InlineKeyboardMarkup(row_width=1)
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b_1 = InlineKeyboardButton(text="ПОЛУЧИТЬ МОЙ ТГ", url="https://web.telegram.org/a/#5281490334")

b_2 = InlineKeyboardButton(text="ПОЛУЧИТЬ МОЙ ВК", url="https://vk.com/id141073311")
b3 = InlineKeyboardButton(text="По какому вопросу?", callback_data="help 1")
# @advokat_Krivachev
kb_1.add(b_1, b_2, b3)

help_b = KeyboardButton("Гражданское право")
help_b1 = KeyboardButton("Семейное право")
help_b2 = KeyboardButton("Уголовное право")
help_b3 = KeyboardButton("Земельное право")
menu_kb.add(help_b,help_b1, help_b2, help_b3)


kb_calendar = InlineKeyboardMarkup(row_width=7)

calendar_1 = [InlineKeyboardButton(text="1 мая", callback_data="1m",
InlineKeyboardButton(text="2 мая", callback_data="2m"),
InlineKeyboardButton(text="3 мая", callback_data="3m"),
InlineKeyboardButton(text="4 мая", callback_data="4m"),
InlineKeyboardButton(text="1 мая", callback_data="5m"),
InlineKeyboardButton(text="1 мая", callback_data="6m"),
InlineKeyboardButton(text="1 мая", callback_data="7m"),
InlineKeyboardButton(text="1 мая", callback_data="8m")]