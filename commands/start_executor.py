from datetime import datetime

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

import data


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.from_user.username
    if username not in data.registered_users:
        data.registered_users[username] = datetime.now()
        await update.message.reply_text(
            f'😁 • Добро пожаловать {username}! Вводи комманду /help для большей информации.'
        )

    reply = ReplyKeyboardMarkup([["/roll", "/profile"], ["/inventory", "/leaderboard"]])

    await update.message.reply_text(
        '🎲 • RNG Game Bot • 🎲\nВерсия бота –› 01v\nАвтор –› @k0cteJl\n\nКоманды:\n/roll - крутить\n/profile - проверить ваш статус\n/inventory - инвентарь (in dev)\n/leaderboard - таблица лидеров',
        reply_markup=reply
    )
