from telegram import Update
from telegram.ext import ContextTypes


async def on_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🍴 • Помощь • 🍴\nИгра из себя представляет RNG подобную игру.\nRNG - это жанр игры в котором всё зависит от рандома.\n\nЧтобы начать игру введи /roll, а далее уже всё будет понятно по ходу игры.")