from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox,
    QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont
from ui.shared.language import t
class ProductView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(t("product_title")) # Düzeltme: t() ile dinamikleştirildi
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Başlık
        self.title = QLabel(t("add_new_product")) # Düzeltme: t() ile dinamikleştirildi
        self.title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        self.title.setObjectName("ProductTitle")

        # Ürün adı
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText(t("product_name"))

        # Kategori
        self.category_input = QComboBox()
        self.category_input.addItems([t("food"), t("beverage"), t("cleaning"), t("other")])

        # Fiyat
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText(t("price_placeholder"))

        # Stok
        self.stock_input = QLineEdit()
        self.stock_input.setPlaceholderText(t("stock_quantity"))

        # Barkod
        self.barcode_input = QLineEdit()
        self.barcode_input.setPlaceholderText(t("barcode_placeholder"))

        # Kaydet butonu
        self.add_btn = QPushButton(t("save_product")) # Düzeltme: t() ile dinamikleştirildi
        self.back_btn = QPushButton(t("back"))
        
        # Üst boşluk
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Form alanları
        layout.addWidget(self.title)
        layout.addWidget(QLabel(t("product_name")))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel(t("category")))
        layout.addWidget(self.category_input)
        layout.addWidget(QLabel(t("price")))
        layout.addWidget(self.price_input)
        layout.addWidget(QLabel(t("stock")))
        layout.addWidget(self.stock_input)
        layout.addWidget(QLabel(t("barcode")))
        layout.addWidget(self.barcode_input)
        layout.addWidget(self.back_btn) # Geri tuşunu da ekleyelim
        # Buton
        layout.addWidget(self.add_btn)
        layout.addWidget(self.back_btn) # Geri tuşunu da ekleyelim

        # Alt boşluk
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Margin ve spacing
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(12)

        self.setLayout(layout)