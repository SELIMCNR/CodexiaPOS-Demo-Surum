from sqlalchemy import Column, Integer, String, Float, DateTime
from core.database import Base, session
from datetime import datetime
from core.database import session


from core.database import get_connection

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    payment_type = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.now)

def save_sale(cart, total, payment_type):
    for product in cart:
        sale = Sale(
            product_name=product["name"],
            price=product["price"],
            payment_type=payment_type,
            date=datetime.now()
        )
        session.add(sale)

    session.commit()


def get_sales_report():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT product_name, price, payment_type, date FROM sales ORDER BY date DESC")
        rows = cursor.fetchall()
        conn.close()
        return [
            {
                "product_name": r[0],
                "price": r[1],
                "payment_type": r[2],
                "date": r[3]
            }
            for r in rows
        ]