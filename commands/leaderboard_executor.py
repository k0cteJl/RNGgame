from telegram import Update
from telegram.ext import ContextTypes

import numpy as np

import data


async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "<b>🎰 Лидеры по круткам 🎰</b>\n"

    spin_amount_leaders = sorted(data.total_spins.items(), key=lambda x: x[1], reverse=True)
    for i, (username, score) in enumerate(spin_amount_leaders[:10], start=1):
        spec_symbol = "🏅 " if i == 1 else "№"
        spec_symbol = "🥈 " if i == 2 else spec_symbol
        spec_symbol = "🥉 " if i == 3 else spec_symbol

        user = update.message.from_user
        word = "прокруток" if score % 10 == 1 else "прокрутка"
        word = "прокрутки" if score % 10 == 2 or score % 10 == 3 or score % 10 == 4 else word
        word = "прокруток" if score % 10 >= 5 or score % 10 == 0 else word

        status = data.users_status[username][0] if username in data.users_status else "Нету статуса."
        status_rarity = " (1/" + str(data.users_status[username][1]) + ")" if user.username in data.users_status else ""

        message += "<blockquote>" if i < 4 else ""
        message += f"<b>{spec_symbol}{i}.</b> [{status}] <i>{status_rarity}</i> {username} - {score} {word}\n"
        message += "</blockquote>" if i < 4 else ""

    for i in range(np.clip(10-len(data.total_spins), 0, 10)):
        n = i + len(data.total_spins) + 1

        spec_symbol = "🏅 " if n == 1 else "№"
        spec_symbol = "🥈 " if n == 2 else spec_symbol
        spec_symbol = "🥉 " if n == 3 else spec_symbol

        message += "<blockquote>" if n < 4 else ""
        message += f"<b>{spec_symbol}{n}.</b> - Пустое место.\n"
        message += "</blockquote>" if n < 4 else ""

    await update.message.reply_text(message, parse_mode="HTML")