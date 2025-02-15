import asyncio
from datetime import datetime
from random import randint

import numpy as np
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import BadRequest
from telegram.ext import ContextTypes

import data

from constants import DROP_LIST, ROLL_COOLDOWN, ROLL_EFFECT
from utils import sqlite
from utils.datashare import SAVED_DATA

from random import randint, choice

def get_random_status(update: Update) -> tuple[str, int]:
    user = update.message.from_user
    if user.is_bot:
        return DROP_LIST[2][0], 2

    chances = sorted(DROP_LIST.keys(), reverse=True)

    for chance in chances:
        random_value = randint(0, chance)
        if random_value == chance:
            status = choice(DROP_LIST[chance])
            return status, chance

    return DROP_LIST[2][0], 2

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    username = update.message.from_user.username

    cooldown = np.ceil(ROLL_COOLDOWN - (datetime.now() - data.users_cooldown[username]).total_seconds()) if username in data.users_cooldown else 0
    if cooldown > 0:
        await update.message.reply_text(f"💢 • Ошибка! • 💢\nКоманду /roll можно использовать раз в 10 секунд.\nПопробуйте снова через {int   (cooldown)} секунд.")
        return

    message = await update.message.reply_text("🎲 • Ожидайте... • 🎲")

    if ROLL_EFFECT:
        await asyncio.sleep(1)

    if username not in data.total_spins:
        data.total_spins[username] = 0
    data.total_spins[username] += 1

    if ROLL_EFFECT:
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
    data.users_cooldown[username] = datetime.now()

    if username not in data.users_roll_history.keys():
        data.users_roll_history[username] = [rnd]
    else:
        data.users_roll_history[username].append(rnd)
        if len(data.users_roll_history[username]) > 10:
            data.users_roll_history[username].pop(0)

    keyboard = [
        [InlineKeyboardButton("Сохранить", callback_data="roll-save"),
         InlineKeyboardButton("Пропустить", callback_data="roll-skip")],
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