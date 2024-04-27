from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
kb_1 = InlineKeyboardMarkup(row_width=1)

b_1 = InlineKeyboardButton(text="ПОЛУЧИ РЕЦЕПТ", url="https://www.russianfood.com/recipes/bytype/?fid=643&ysclid=lvi4ea80st184033379")
b_2 = InlineKeyboardButton(text="ПОЛУЧИТЬ СЛУЧАЙНОЕ ЧИСЛО", callback_data="☻")
b_3 = InlineKeyboardButton(text="ДРУГАЯ КНОПКА", callback_data="fgh")
kb_1.add(b_1, b_2, b_3)
