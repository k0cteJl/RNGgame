from telegram import Update
from telegram.ext import ContextTypes


async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return