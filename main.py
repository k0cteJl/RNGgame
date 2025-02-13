from constants import *

from commands.start_executor import start
from commands.roll_executor import roll
from commands.profile_executor import profile
from commands.message_executor import on_message

from telegram.ext import Application, CommandHandler, MessageHandler, filters

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("roll", roll))
    application.add_handler(CommandHandler("profile", profile))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))

    application.run_polling()

if __name__ == '__main__':
    main()