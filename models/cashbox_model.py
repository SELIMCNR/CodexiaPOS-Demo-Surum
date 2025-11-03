from sqlalchemy import Column, Integer, String, Float, DateTime
from core.database import Base
from datetime import datetime

class CashboxTransaction(Base):
    __tablename__ = "cashbox_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)          # "sale", "refund", "manual"
    amount = Column(Float, nullable=False)
    payment_type = Column(String, nullable=False)  # "cash", "card"
    timestamp = Column(DateTime, default=datetime.now)

class CashboxClosure(Base):
    __tablename__ = "cashbox_closures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String, nullable=False)          # YYYY-MM-DD
    total = Column(Float, nullable=False)
    cash = Column(Float, nullable=False)
    card = Column(Float, nullable=False)