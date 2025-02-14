from telegram import Update
from telegram.ext import ContextTypes

import numpy as np

import data


async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "🗽 • Таблица лидеров • 🗽\n\n🎰 Лидеры по колличеству /roll 🎰\n"

    spin_amount_leaders = sorted(data.total_spins.items(), key=lambda x: x[1], reverse=True)
    for i, (username, score) in enumerate(spin_amount_leaders[:5], start=1):
        spec_symbol = "🏅 " if i == 1 else "№"
        spec_symbol = "🥈 " if i == 2 else spec_symbol
        spec_symbol = "🥉 " if i == 3 else spec_symbol

        user = update.message.from_user
        message += f"{spec_symbol}{i}. [{data.users_status[user.username] if user.username in data.users_status else "Нету статуса."}] {username} - {score} {"прокруток" if score != 1 else "прокрутка"}\n"

    for i in range(np.clip(5-len(data.total_spins), 0, 5)):
        message += "🪨 - Пустое место.\n"

    await update.message.reply_text(message)