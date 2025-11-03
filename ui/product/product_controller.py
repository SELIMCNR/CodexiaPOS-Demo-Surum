import random
from PyQt6.QtWidgets import QMessageBox
from core.barcode import generate_barcode
from models.product_model import save_product

class ProductController:
    def __init__(self, view, return_callback):
        self.view = view
        self.return_callback = return_callback
        self.view.add_btn.clicked.connect(self.save_product)
        self.view.back_btn.clicked.connect(self.return_callback)  # ❌ ama back_btn yoksa hata verir
 
    def save_product(self):
        try:
            name = self.view.name_input.text().strip()
            category = self.view.category_input.currentText()
            price_text = self.view.price_input.text().strip()
            stock_text = self.view.stock_input.text().strip()
            barcode = self.view.barcode_input.text().strip()

            # Zorunlu alan kontrolü
            if not name or not price_text or not stock_text:
                QMessageBox.warning(self.view, "Eksik Bilgi", "Lütfen tüm zorunlu alanları doldurun.")
                return

            # Sayısal değer kontrolü
            try:
                price = float(price_text)
                stock = int(stock_text)
            except ValueError:
                QMessageBox.warning(self.view, "Hatalı Veri", "Fiyat ve stok sayısal olmalıdır.")
                return

            # Barkod boşsa otomatik üret
            if not barcode:
                raw_code = str(random.randint(100000000000, 999999999999))  # 12 haneli
                barcode, filepath = generate_barcode(raw_code, name.replace(" ", "_"))
                print(f"Barkod görseli kaydedildi: {filepath}")

            # Ürünü DB’ye kaydet
            save_product(name, category, price, stock, barcode)

            QMessageBox.information(self.view, "Başarılı", f"Ürün başarıyla kaydedildi.\nBarkod: {barcode}")

            # Formu temizle
            self.view.name_input.clear()
            self.view.price_input.clear()
            self.view.stock_input.clear()
            self.view.barcode_input.clear()
            self.view.category_input.setCurrentIndex(0)

        except Exception as e:
            QMessageBox.critical(self.view, "Hata", f"Ürün kaydedilirken hata oluştu:\n{str(e)}")