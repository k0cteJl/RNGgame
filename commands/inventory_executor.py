from telegram import Update
from telegram.ext import ContextTypes


async def inventory(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("В разработке!")