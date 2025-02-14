import asyncio
from random import randint

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import BadRequest
from telegram.ext import ContextTypes

import data

from constants import DROP_LIST
from utils import sqlite
from utils.datashare import SAVED_DATA


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
    if username not in data.total_spins:
        data.total_spins[username] = 0
    data.total_spins[username] += 1

    combo: int = 1
    previous_text = None

    for _ in range(25):
        rnd = get_random_status(update)
        text = rnd[0]
        change = rnd[1]

        new_message = f"🎲 • Крутим... \n1/{change} - {text}"
        if previous_text == new_message:
            combo += 1
            new_message = f"🎲 • Крутим... \n1/{change} - {text} (x{combo})"
        else:
            combo = 1

        try:
            await message.edit_text(new_message)
            previous_text = new_message
        except BadRequest as e:
            print(e)

        await asyncio.sleep(0.1)

    rnd = get_random_status(update)

    user = update.message.from_user

    if user.username not in data.users_roll_history.keys():
        data.users_roll_history[user.username] = [rnd]
    else:
        data.users_roll_history[user.username].append(rnd)
        if len(data.users_roll_history[user.username]) > 10:
            data.users_roll_history[user.username].pop(0)

    keyboard = [
        [InlineKeyboardButton("Сохранить", callback_data="roll-save")],
        [InlineKeyboardButton("Пропустить", callback_data="roll-skip")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    SAVED_DATA[f"{username}-roll-rnd"] = rnd

    await message.edit_text(f"💫 • Вы получили: {rnd[0]} (1/{rnd[1]})", reply_markup=reply_markup)

async def roll_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.callback_query.from_user.username
    query_data = update.callback_query.data
    if query_data == "roll-save":
        rnd = SAVED_DATA[f"{username}-roll-rnd"]
        data.users_status[username] = rnd
        await update.callback_query.edit_message_text(text=f'😍 • Вы успешно сохранили новый титул!\n💫 • Новый статус: {rnd[0]} (1/{rnd[1]})', reply_markup=None)
    elif query_data == "roll-skip":
        await update.callback_query.edit_message_text(text=f'🚽 • Титул был удалён', reply_markup=None)

    sqlite.save_user(username)