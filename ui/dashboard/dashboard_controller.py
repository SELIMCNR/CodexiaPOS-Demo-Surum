class DashboardController:
    def __init__(self, view, on_sales, on_product, on_report, on_settings, on_cashbox, return_callback):
       
        self.view = view
        self.return_callback = return_callback
        self.on_sales = on_sales
        self.on_product = on_product
        self.on_report = on_report
        self.on_settings = on_settings
        self.on_cashbox = on_cashbox  # Gerekli olmasa da tutulması iyi

        # Butonları fonksiyonlara bağla
        self.view.sales_btn.clicked.connect(self.on_sales)
        self.view.product_btn.clicked.connect(self.on_product)
        self.view.report_btn.clicked.connect(self.on_report)
        self.view.settings_btn.clicked.connect(self.on_settings)
        self.view.cashbox_btn.clicked.connect(self.on_cashbox) # Düzeltme: self.view eklendi ve self.on_cashbox'a bağlandı