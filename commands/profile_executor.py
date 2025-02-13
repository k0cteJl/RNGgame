from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

from data import users_status, registered_users, total_spins


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user

    display_name = user.first_name + " " + user.last_name
    registration_date = registered_users[user.username] if user.username in registered_users else '/start'
    status = users_status[user.username] if user.username in users_status else "Пусто..."
    total_user_spins = total_spins[user.username] if user.username in total_spins else 0

    delta = datetime.now() - registration_date if registration_date != '/start' else '/start'

    total_hours = f"{delta.total_seconds() // 3600}ч." if delta != '/start' else '/start'
    display_registration_date = registration_date.date() if registration_date != '/start' else '/start'

    await update.message.reply_text(
        f"""👤 • Профиль • 👤
        
💌 Имя: {display_name}
🎲 Статус: {status[0] + " (1/" + str(status[1]) + ")" if status != "Пусто..." else status}
🎲 Колличество круток: {total_user_spins}
        
🕒 Время существования аккаунта: {total_hours}
🕒 Время регистрации: {display_registration_date}
        """
    )