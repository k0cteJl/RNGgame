import asyncio
from random import randint

from telegram import Update
from telegram.error import BadRequest
from telegram.ext import ContextTypes

from constants import DROP_LIST
from data import users_status, users_roll_history, total_spins


def get_random_status(update: Update) -> tuple[str, int]:
    user = update.message.from_user
    if user.is_bot:
        return DROP_LIST[2][0], 2

    status_chance = 2
    status = DROP_LIST[2][randint(0, len(DROP_LIST[2])-1)]
    for chance in DROP_LIST.keys():
        i = randint(1, chance)
        if i == chance // 2:
            status_chance = chance
            status = DROP_LIST[chance][randint(0, len(DROP_LIST[chance])-1)]
            break
    return status, status_chance

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = await update.message.reply_text("🎲 • Начинаем! • 🎲")

    await asyncio.sleep(1)

    username = update.message.from_user.username
    if username not in total_spins:
        total_spins[username] = 0
    total_spins[username] += 1

    combo: int = 1
    for _ in range(25):
        rnd = get_random_status(update)
        text = rnd[0]
        change = rnd[1]

        new_message = f"🎲 • Крутим... \n1/{change} - {text}"
        if message.text == new_message:
            combo += 1
            new_message = f"🎲 • Крутим... \n1/{change} - {text} (x{combo})"
        else:
            combo = 1

        try:
            await message.edit_text(new_message)
        except BadRequest as e:
            print(e)

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

    await message.edit_text(f"💫 • Вы получили статус: {rnd[0]} (1/{rnd[1]})")