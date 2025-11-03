from core.database import get_connection
from config.settings import DB_PATH

def save_product(name, category, price, stock, barcode):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (name, category, price, stock, barcode)
        VALUES (?, ?, ?, ?, ?)
    """, (name, category, price, stock, barcode))
    conn.commit()
    conn.close()

def get_product_by_barcode(barcode):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM products WHERE barcode = ?", (barcode.strip(),))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"name": result[0], "price": result[1]}
    return None

def update_stock(barcode, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET stock = stock - ? WHERE barcode = ?", (quantity, barcode))
    conn.commit()
    conn.close()

def get_stock_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, stock, category FROM products ORDER BY stock ASC")
    rows = cursor.fetchall()
    conn.close()
    return [{"name": r[0], "stock": r[1], "category": r[2]} for r in rows]