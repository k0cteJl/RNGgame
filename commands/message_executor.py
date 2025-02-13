from telegram import Update
from telegram.ext import ContextTypes


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    await update.message.reply_text(f'Вы сказали: {user_text}')