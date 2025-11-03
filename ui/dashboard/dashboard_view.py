from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel,
    QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont
from ui.shared.language import t

class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(t("dashboard_title"))  # ✅ key kullanıldı
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Başlık
        self.title = QLabel(t("dashboard_title"))  # ✅ key kullanıldı
        self.title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        self.title.setObjectName("DashboardTitle")

        # Butonlar
        self.sales_btn = QPushButton(t("sales_screen"))     # ✅
        self.product_btn = QPushButton(t("product_screen")) # ✅
        self.report_btn = QPushButton(t("report_screen"))   # ✅
        self.settings_btn = QPushButton(t("settings_screen")) # ✅
        self.cashbox_btn = QPushButton(t("cashbox_screen"))
        self.back_btn = QPushButton(t("back"))

        # Üst boşluk
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Başlık
        layout.addWidget(self.title)
   

        # Butonlar
        layout.addWidget(self.sales_btn)
        layout.addWidget(self.product_btn)
        layout.addWidget(self.cashbox_btn)
        layout.addWidget(self.report_btn)
        layout.addWidget(self.settings_btn)

        # Alt boşluk
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Margin ve spacing
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(15)

        self.setLayout(layout)