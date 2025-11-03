from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from ui.shared.language import t

class ReportsView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            t("product_name"),
            t("price"),
            t("payment_type"),
            t("date")
        ])
        layout.addWidget(self.table)

        self.back_btn = QPushButton(t("back"))
        layout.addWidget(self.back_btn)

        self.setLayout(layout)