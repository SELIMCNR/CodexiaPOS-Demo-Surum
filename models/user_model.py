from core.database import get_connection
from core.security import hash_password
import sqlite3

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, hashed_password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"username": result[0], "hashed_password": result[1]}
    return None

def create_user(username, password, role="kasiyer"):
    conn = get_connection()
    cursor = conn.cursor()
    hashed = hash_password(password)
    try:
        cursor.execute(
            "INSERT INTO users (username, hashed_password, role) VALUES (?, ?, ?)",
            (username, hashed, role)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Kullanıcı zaten var: {username}")
    finally:
        conn.close()