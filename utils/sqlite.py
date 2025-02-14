import sqlite3
from datetime import datetime

import data


def create_tables() -> None:
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            registration_date TEXT,
            total_spins INTEGER
        )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_status (
            username TEXT PRIMARY KEY,  -- Добавлен первичный ключ
            title TEXT,
            chance INTEGER,
            FOREIGN KEY(username) REFERENCES users(username)
        )
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS roll_history (
            roll_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            title TEXT,
            chance INTEGER,
            roll_date TEXT,
            FOREIGN KEY(username) REFERENCES users(username)
        )
        """)

    conn.commit()
    conn.close()

def load():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    users_status = {}
    users_roll_history = {}
    registered_users = {}
    total_spins = {}

    cursor.execute("SELECT * FROM users")
    for username, reg_date, spins in cursor.fetchall():
        registered_users[username] = datetime.fromisoformat(reg_date)
        total_spins[username] = spins

    cursor.execute("SELECT * FROM user_status")
    for username, title, chance in cursor.fetchall():
        users_status[username] = (title, chance)

    cursor.execute("SELECT * FROM roll_history")
    for _, username, title, chance, _ in cursor.fetchall():
        if username not in users_roll_history:
            users_roll_history[username] = []
        users_roll_history[username].append((title, chance))

    conn.close()
    return users_status, users_roll_history, registered_users, total_spins

def save_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Начало транзакции
    conn.execute("BEGIN TRANSACTION")

    # Сохраняем основную информацию о пользователе
    total_spins_value = data.total_spins.get(username, 0)
    cursor.execute("""
                INSERT OR REPLACE INTO users (username, registration_date, total_spins)
                VALUES (?, ?, ?)
            """, (username, data.registered_users[username].isoformat(), total_spins_value))

    # Сохраняем статус пользователя
    title = data.users_status[username][0]
    chance = data.users_status[username][1]
    cursor.execute("""
                INSERT OR REPLACE INTO user_status (username, title, chance)
                VALUES (?, ?, ?)
            """, (username, title, chance))

    # Сохраняем историю прокруток
    rolls = data.users_roll_history[username]
    for title, chance in rolls:
        cursor.execute("""
                    INSERT INTO roll_history (username, title, chance, roll_date)
                    VALUES (?, ?, ?, ?)
                """, (username, title, chance, datetime.now().isoformat()))

    # Удаляем старые записи, оставляя только последние 10
    cursor.execute("""
                DELETE FROM roll_history
                WHERE username = ? AND roll_id NOT IN (
                    SELECT roll_id FROM roll_history
                    WHERE username = ?
                    ORDER BY roll_date DESC
                    LIMIT 10
                )
            """, (username, username))

    conn.commit()
    conn.close()