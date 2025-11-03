from PyQt6.QtWidgets import QWidget, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout
from ui.shared.language import t

class CashboxView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(t("cashbox_screen"))
        
        self.init_ui()

    def init_ui(self):
        self.total_label = QLabel(f"{t('total_sales')}: ₺0.00")
        self.cash_label = QLabel(f"{t('cash_total')}: ₺0.00")
        self.card_label = QLabel(f"{t('card_total')}: ₺0.00")

        self.transaction_table = QTableWidget()
        self.transaction_table.setColumnCount(3)
        self.transaction_table.setHorizontalHeaderLabels([
            t("transaction_type"), t("amount"), t("timestamp")
        ])

        self.close_day_btn = QPushButton(t("close_day"))
        self.export_btn = QPushButton(t("export_report"))
        self.back_btn = QPushButton(t("back"))

        layout = QVBoxLayout()
        layout.addWidget(self.total_label)
        layout.addWidget(self.cash_label)
        layout.addWidget(self.card_label)
        layout.addWidget(self.transaction_table)
        layout.addWidget(self.close_day_btn)
        layout.addWidget(self.export_btn)
        layout.addWidget(self.back_btn)
        self.setLayout(layout)