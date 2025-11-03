from models.sales_model import get_sales_report
from PyQt6.QtWidgets import QTableWidgetItem
from ui.shared.language import t

class ReportsController:
    def __init__(self, view, return_callback):
        self.view = view
        self.return_callback = return_callback

        self.view.back_btn.clicked.connect(self.return_callback)
        self.load_report()

    def load_report(self):
        data = get_sales_report()
        self.view.table.setRowCount(len(data))

        for i, row in enumerate(data):
            self.view.table.setItem(i, 0, QTableWidgetItem(row["product_name"]))
            self.view.table.setItem(i, 1, QTableWidgetItem(f"₺{row['price']:.2f}"))
            self.view.table.setItem(i, 2, QTableWidgetItem(row["payment_type"]))
            self.view.table.setItem(i, 3, QTableWidgetItem(row["date"]))