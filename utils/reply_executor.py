from telegram import Update
from telegram.ext import ContextTypes

from commands.roll_executor import roll_reply


async def reply_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    query_id = query.data.split("-", 1)[0]

    if query_id == "roll":
        await roll_reply(update, context)