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
        username TEXT,
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

def save() -> None:
    from data import users_status, users_roll_history, registered_users, total_spins

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    for username, reg_date in registered_users.items():
        total_spins_value = total_spins.get(username, 0)
        cursor.execute("""
        INSERT OR REPLACE INTO users (username, registration_date, total_spins)
        VALUES (?, ?, ?)
        """, (username, reg_date.isoformat(), total_spins_value))

    for username, (title, chance) in users_status.items():
        cursor.execute("""
        INSERT OR REPLACE INTO user_status (username, title, chance)
        VALUES (?, ?, ?)
        """, (username, title, chance))

    for username, rolls in users_roll_history.items():
        for title, chance in rolls:
            cursor.execute("""
            INSERT INTO roll_history (username, title, chance, roll_date)
            VALUES (?, ?, ?, ?)
            """, (username, title, chance, datetime.now().isoformat()))

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

    total_spins_value = data.total_spins.get(username, 0)
    cursor.execute("""
        INSERT OR REPLACE INTO users (username, registration_date, total_spins)
        VALUES (?, ?, ?)
        """, (username, data.registered_users[username].isoformat(), total_spins_value))

    title = data.users_status[username][0]
    chance = data.users_status[username][1]
    cursor.execute("""
        INSERT OR REPLACE INTO user_status (username, title, chance)
        VALUES (?, ?, ?)
        """, (username, title, chance))

    rolls = data.users_roll_history[username]
    for title, chance in rolls:
        cursor.execute("""
            INSERT INTO roll_history (username, title, chance, roll_date)
            VALUES (?, ?, ?, ?)
            """, (username, title, chance, datetime.now().isoformat()))

    conn.commit()
    conn.close()