from aiogram.types import InlineKeyboardMarkup


async def create_keyboard(buttons, row_width=2):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            buttons[i : i + row_width] for i in range(0, len(buttons), row_width)
        ]
    )
