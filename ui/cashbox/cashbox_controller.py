from models.cashbox_model import CashboxTransaction, CashboxClosure
from core.database import session
from PyQt6.QtWidgets import QMessageBox,QTableWidgetItem
from datetime import datetime
from ui.shared.language import t
class CashboxController:
    def __init__(self, view, return_callback):
        self.view = view
        self.return_callback = return_callback
        self.load_data()
        
        self.view.close_day_btn.clicked.connect(self.close_day)
        self.view.export_btn.clicked.connect(self.export_report)
        self.view.back_btn.clicked.connect(self.return_callback)  # ❌ ama back_btn yoksa hata verir
    def load_data(self):
        today = datetime.now().strftime("%Y-%m-%d")
        transactions = session.query(CashboxTransaction).filter(
            CashboxTransaction.timestamp.like(f"{today}%")
        ).all()

        total = sum(tx.amount for tx in transactions)
        cash = sum(tx.amount for tx in transactions if tx.payment_type == "cash")
        card = sum(tx.amount for tx in transactions if tx.payment_type == "card")

        self.view.total_label.setText(f"{t('total_sales')}: ₺{total:.2f}")
        self.view.cash_label.setText(f"{t('cash_total')}: ₺{cash:.2f}")
        self.view.card_label.setText(f"{t('card_total')}: ₺{card:.2f}")

        self.view.transaction_table.setRowCount(len(transactions))
        for i, tx in enumerate(transactions):
            self.view.transaction_table.setItem(i, 0, QTableWidgetItem(tx.type))
            self.view.transaction_table.setItem(i, 1, QTableWidgetItem(f"₺{tx.amount:.2f}"))
            self.view.transaction_table.setItem(i, 2, QTableWidgetItem(tx.timestamp.strftime("%H:%M:%S")))

    def close_day(self):
        today = datetime.now().strftime("%Y-%m-%d")
        existing = session.query(CashboxClosure).filter_by(date=today).first()
        if existing:
            QMessageBox.warning(self.view, t("day_closed"), t("already_closed"))
            return

        transactions = session.query(CashboxTransaction).filter(
            CashboxTransaction.timestamp.like(f"{today}%")
        ).all()

        total = sum(tx.amount for tx in transactions)
        cash = sum(tx.amount for tx in transactions if tx.payment_type == "cash")
        card = sum(tx.amount for tx in transactions if tx.payment_type == "card")

        closure = CashboxClosure(date=today, total=total, cash=cash, card=card)
        session.add(closure)
        session.commit()

        QMessageBox.information(self.view, t("day_closed"), t("cashbox_closed_success"))

    def export_report(self):
        # Buraya PDF/Excel dışa aktarım fonksiyonu entegre edilebilir
        QMessageBox.information(self.view, t("export_report"), t("report_exported"))