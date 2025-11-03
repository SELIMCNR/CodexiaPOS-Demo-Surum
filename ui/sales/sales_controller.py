from models.product_model import get_product_by_barcode, update_stock
from models.sales_model import save_sale
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QTableWidgetItem, QVBoxLayout, QLabel, QComboBox
from models.cashbox_model import CashboxTransaction
from core.database import session

class SalesController:
    def __init__(self, view, return_callback):
        self.view = view
        self.return_callback = return_callback
        self.cart = []
        self.total = 0.0

        # Event bağlama
        self.view.add_btn.clicked.connect(self.add_product)
        self.view.complete_btn.clicked.connect(self.complete_sale)
        self.view.barcode_input.returnPressed.connect(self.trigger_add)
        self.view.back_btn.clicked.connect(self.return_callback)  # ❌ ama back_btn yoksa hata verir
 
    def trigger_add(self):
        self.add_product()
        self.view.barcode_input.clear()
        self.view.barcode_input.setFocus()

    def add_product(self):
        barcode = self.view.barcode_input.text().strip()
        print("Okunan barkod:", barcode)
        product = get_product_by_barcode(barcode)
        if product:
            self.cart.append(product)
            self.total += product["price"]

            # Tabloya yeni satır ekle
            row = self.view.table.rowCount()
            self.view.table.insertRow(row)
            self.view.table.setItem(row, 0, QTableWidgetItem(product["name"]))
            self.view.table.setItem(row, 1, QTableWidgetItem(f"₺{product['price']:.2f}"))
            self.view.table.setItem(row, 2, QTableWidgetItem("1"))

            # Toplam güncelle
            self.view.total_label.setText(f"Toplam: ₺{self.total:.2f}")

            # stok düşür
            update_stock(barcode, 1)
        else:
            print("Ürün bulunamadı")

    def complete_sale(self):
        payment = self.view.payment_type.currentText()
        save_sale(self.cart, self.total, payment)

        # Kasa kaydı ekle
        transaction = CashboxTransaction(
            type="sale",
            amount=self.total,
            payment_type=payment
        )
        session.add(transaction)
        session.commit()

        # Temizle
        self.cart.clear()
        self.total = 0.0
        self.view.table.setRowCount(0)
        self.view.total_label.setText("Toplam: ₺0.00")