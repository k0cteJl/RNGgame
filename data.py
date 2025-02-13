from datetime import datetime

users_status = {}
users_roll_history: dict[str, list[tuple[str, int]]] = {}

registered_users: dict[str, datetime] = {}
total_spins: dict[str, int] = {}

def save_to_sql():
    pass

def load_from_sql():
    pass