from datetime import datetime

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from data import registered_users


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.from_user.username
    if username not in registered_users:
        registered_users[username] = datetime.now()
        await update.message.reply_text(
            f'😁 • Добро пожаловать {username}!'
        )

    reply = ReplyKeyboardMarkup([["/roll", "/profile"]])

    await update.message.reply_text(
        '🎲 • RNG Game Bot • 🎲\nВерсия бота –› 01v\nАвтор –› @k0cteJl\n\nКоманды:\n/roll - крутить\n/profile - проверить ваш статус',
        reply_markup=reply
    )
