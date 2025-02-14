import sqlite3

from commands.leaderboard_executor import leaderboard
from constants import *

from commands.start_executor import start
from commands.roll_executor import roll
from commands.profile_executor import profile
from commands.inventory_executor import inventory
from commands.message_executor import on_message
from utils.sqlite import create_tables, load

from utils.reply_executor import reply_click

from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

import data


def main() -> None:
    try:
        data.users_status, data.users_roll_history, data.registered_users, data.total_spins = load()
    except sqlite3.Error as e:
        print(f":):\n{e}")
        create_tables()
        data.users_status, data.users_roll_history, data.registered_users, data.total_spins = load()

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("roll", roll))
    application.add_handler(CommandHandler("profile", profile))
    application.add_handler(CommandHandler("inventory", inventory))
    application.add_handler(CommandHandler("leaderboard", leaderboard))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    application.add_handler(CallbackQueryHandler(reply_click))

    application.run_polling()

if __name__ == '__main__':
    main()