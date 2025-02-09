"""

ОПРАВДАНИЯ НА СЧЁТ ПРОЕКТА
1) Я его делал 1 часик от силы, потому что с головой занят другим (если что, другой проект никак не подойдёт для ИП)
2) RNG - ЭТО НЕ КАЗИНО И НИКАК НЕ СВЯЗАН. Игровой процесс завязан на случайно сгенерированных числах.
0x0011) Я Радмир или Ильшат, как мне сказала мама
0x0100) Документация (зачем-то) в README.TXT
5) Проект еле живой и я тут очень захардкодил (+в одном файле)
6) БД будет, на след. или след. след. паре (ну короче, когда мне лень не будет)

"""

import asyncio
from random import randint

from telegram import Update
from telegram.error import BadRequest
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = '8112259004:AAG-H854Mhy1G4j0KMrI_mJIlY4wMaqs-2Y'

users_status = {}
users_roll_history: dict[str, list[tuple[str, int]]] = {}

all_status_list = {
    2:["Обычный"],
    4:["Необычный"],
    8:["Редкий"],
    12:["Очень редкий"],
    20:["Эпический"],
    30:["Легендарный"]
}

def get_random_status(update: Update) -> tuple[str, int]:
    user = update.message.from_user
    if user.is_bot:
        return all_status_list[2][0], 2

    status_chance = 2
    status = all_status_list[2][randint(0, len(all_status_list[2])-1)]
    for chance in all_status_list.keys():
        i = randint(1, chance)
        if i == chance // 2:
            status_chance = chance
            status = all_status_list[chance][randint(0, len(all_status_list[chance])-1)]
            break
    return status, status_chance

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('🎲 RNG Game Bot 🎲\n/roll - крутить\n/check_status - проверить ваш статус')


async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = await update.message.reply_text("🎲: 1/2 - Обычный")

    combo: int = 1
    for _ in range(25):
        rnd = get_random_status(update)
        text = rnd[0]
        change = rnd[1]

        new_message = f"🎲: 1/{change} - {text}"
        if message.text == new_message:
            combo += 1
            new_message = f"🎲: 1/{change} - {text} (x{combo})"
        else:
            combo = 1

        try:
            if new_message != message.text:  # Проверяем, изменился ли текст
                await message.edit_text(new_message)
        except BadRequest as e:
            print(f"Ошибка при редактировании сообщения: {e}")

        await asyncio.sleep(0.1)

    rnd = get_random_status(update)

    user = update.message.from_user
    users_status[user.username] = rnd

    if user.username not in users_roll_history.keys():
        users_roll_history[user.username] = [rnd]
    else:
        users_roll_history[user.username].append(rnd)
        if len(users_roll_history[user.username]) > 10:
            users_roll_history[user.username].pop(0)

    await message.edit_text(f"🎲 Ты получил статус '{rnd[0]}' с шансом 1 к {rnd[1]}")
    print(f"""

    Данные изменились!
    users_status: {users_status}
    users_roll_history: {users_roll_history}

    """)

async def check_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    if user.username in users_status:
        status = users_status[user.username]
        await update.message.reply_text(f"Ваш статус: '{status[0]}' с шансом 1 к {status[1]}")
    else:
        await update.message.reply_text("У вас пока нет статуса. Используйте /roll, чтобы получить его.")

async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    await update.message.reply_text(f'Вы сказали: {user_text}')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("roll", spin))
    application.add_handler(CommandHandler("check_status", check_status))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))

    application.run_polling()

if __name__ == '__main__':
    main()