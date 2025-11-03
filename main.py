import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from config import settings
from core.database import session
from models.sales_model import Sale
from datetime import datetime
# UI Modülleri
from ui.login.login_view import LoginView
from ui.login.login_controller import LoginController
from ui.dashboard.dashboard_view import DashboardView
from ui.sales.sales_view import SalesView
from ui.sales.sales_controller import SalesController
from ui.product.product_view import ProductView
from ui.product.product_controller import ProductController
from ui.settings.settings_view import SettingsView
from ui.settings.settings_controller import SettingsController
from ui.reports.reports_view import ReportsView
from ui.reports.reports_controller import ReportsController
from ui.cashbox.cashbox_view import CashboxView
from ui.cashbox.cashbox_controller import CashboxController

# Ortak modüller
from ui.shared.language import t
from core.database import init_db
from models.user_model import create_user

class CodexiaPOSApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Veritabanı tablolarını oluştur
        init_db()
        create_user("admin", "1234", "admin")

        # Uygulama ayarları
        self.setWindowIcon(QIcon("assets/icons/app.png"))
        self.resize(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        self.setMinimumSize(800, 600)

        # Tema uygula
        self.apply_theme(settings.DEFAULT_THEME)

        # İlk ekran: Login
        self.login_view = LoginView()
        self.login_controller = LoginController(self.login_view, self.show_dashboard)
        self.setCentralWidget(self.login_view)
        self.show()

    def apply_theme(self, theme):
        try:
            path = os.path.join("assets", "styles", f"{theme}.qss")
            with open(path, "r", encoding="utf-8") as f:
                qss = f.read()
                QApplication.instance().setStyleSheet(qss)
        except Exception as e:
            print("Tema yükleme hatası:", e)
            QApplication.instance().setStyleSheet("")

    def show_dashboard(self, user=None):
        self.dashboard_view = DashboardView()
        self.dashboard_view.sales_btn.clicked.connect(self.show_sales)
        self.dashboard_view.product_btn.clicked.connect(self.show_product)
        self.dashboard_view.report_btn.clicked.connect(self.show_reports)
        self.dashboard_view.settings_btn.clicked.connect(self.show_settings)
        self.dashboard_view.cashbox_btn.clicked.connect(self.show_cashbox)
        self.setCentralWidget(self.dashboard_view)

    def show_sales(self):
        self.sales_view = SalesView()
        self.sales_controller = SalesController(self.sales_view, self.show_dashboard)
        self.setCentralWidget(self.sales_view)

    def show_product(self):
        self.product_view = ProductView()
        self.product_controller = ProductController(self.product_view, self.show_dashboard)
        self.setCentralWidget(self.product_view)

    def show_reports(self):
        self.reports_view = ReportsView()
        self.reports_controller = ReportsController(self.reports_view, self.show_dashboard)
        self.setCentralWidget(self.reports_view)

    def show_cashbox(self):
        self.cashbox_view = CashboxView()
        self.cashbox_controller = CashboxController(self.cashbox_view, self.show_dashboard)
        self.setCentralWidget(self.cashbox_view)
    def update_stock(barcode, quantity):
        product = session.query(ProductController).filter_by(barcode=barcode).first()
        if product:
            product.stock -= quantity
            session.commit()    
    def save_sale(cart, total, payment_type):
     

        for product in cart:
            sale = Sale(
                product_name=product["name"],
                price=product["price"],
                payment_type=payment_type,
                date=datetime.now()
            )
            session.add(sale)

        session.commit()
    def show_settings(self):
        self.settings_view = SettingsView()
        self.settings_controller = SettingsController(
            self.settings_view,
            self.refresh_ui,
            self,
            self.show_dashboard  # ← eksik olan parametre bu
        )
        self.setCentralWidget(self.settings_view)
    def refresh_ui(self):
        widget = self.centralWidget()

        if isinstance(widget, DashboardView):
            widget.setWindowTitle(t("dashboard_title"))
            widget.sales_btn.setText(t("sales_screen"))
            widget.product_btn.setText(t("product_screen"))
            widget.report_btn.setText(t("report_screen"))
            widget.settings_btn.setText(t("settings_screen"))
            widget.cashbox_btn.setText(t("cashbox_screen"))

        elif isinstance(widget, SalesView):
            widget.setWindowTitle(t("sales_screen"))
            widget.total_label.setText(f"{t('total')}: ₺0.00")
            widget.complete_btn.setText(t("complete_sale"))
            widget.payment_type.clear()
            widget.payment_type.addItems([t("payment_cash"), t("payment_card")])
            widget.back_btn.setText(t("back"))

        elif isinstance(widget, ProductView):
            widget.setWindowTitle(t("product_screen"))
            widget.add_btn.setText("Ürünü Kaydet" if t("product_screen") == "Ürün Yönetimi" else "Save Product")
            widget.back_btn.setText(t("back"))

        elif isinstance(widget, ReportsView):
            widget.setWindowTitle(t("report_screen"))
            widget.back_btn.setText(t("back"))

        elif isinstance(widget, CashboxView):
            widget.setWindowTitle(t("cashbox_screen"))
            widget.back_btn.setText(t("back"))

        elif isinstance(widget, SettingsView):
            widget.setWindowTitle(t("settings_screen"))
            widget.save_btn.setText("Kaydet" if t("settings_screen") == "Ayarlar" else "Save")
            widget.back_btn.setText(t("back"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CodexiaPOSApp()
    sys.exit(app.exec())