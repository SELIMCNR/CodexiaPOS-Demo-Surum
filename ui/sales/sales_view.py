from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QPushButton, QTableWidget, QVBoxLayout, QLabel, QComboBox,
    QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont
from ui.shared.language import t
class SalesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Satış Ekranı")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Başlık
        self.title = QLabel("Satış Ekranı")
        self.title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        self.title.setObjectName("SalesTitle")
      
        # Barkod girişi
        self.barcode_input = QLineEdit()
        self.barcode_input.setPlaceholderText("Barkod okutun...")

        # Ürün ekle butonu
        self.add_btn = QPushButton("Ürünü Ekle")
        self.back_btn = QPushButton(t("back"))
        # Satış tablosu
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Ürün Adı", "Fiyat", "Adet"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setDefaultSectionSize(150)

        # Toplam label
        self.total_label = QLabel("Toplam: ₺0.00")
        self.total_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))

        # Ödeme türü
        self.payment_type = QComboBox()
        self.payment_type.addItems(["Nakit", "Kart"])

        # Satışı tamamla butonu
        self.complete_btn = QPushButton("Satışı Tamamla")

        # Üst boşluk
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Başlık ve form alanları
        layout.addWidget(self.title)
        layout.addWidget(self.barcode_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.table)
        layout.addWidget(self.total_label)
        layout.addWidget(QLabel("Ödeme Türü"))
        layout.addWidget(self.payment_type)
        layout.addWidget(self.complete_btn)
        layout.addWidget(self.back_btn) # Geri tuşunu da ekleyelim
        # Alt boşluk
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Margin ve spacing
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(15)

        self.setLayout(layout)