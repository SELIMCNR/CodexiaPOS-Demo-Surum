import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine("sqlite:///codexia.db", echo=False)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


DB_NAME = "codexia.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
   
    # Diğer modeller buraya eklenebilir
    Base.metadata.create_all(bind=engine)

    conn = get_connection()
    cursor = conn.cursor()
    Base.metadata.create_all(bind=engine)
    # Kullanıcı tablosu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        hashed_password BLOB NOT NULL,
        role TEXT DEFAULT 'kasiyer'
    )
    """)

    # Ürün tablosu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price REAL NOT NULL,
        stock INTEGER DEFAULT 0,
        barcode TEXT UNIQUE
    )
    """)

    # Satış tablosu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        price REAL,
        payment_type TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()