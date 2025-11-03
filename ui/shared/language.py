LANG = "tr"

translations = {
    "tr": {
        "settings_screen": "Ayarlar",
        "sales_screen": "Satış Ekranı",
        "product_screen": "Ürün Yönetimi",
        "report_screen": "Raporlar",
        "dashboard_title": "CodexiaPOS Dashboard",
        "complete_sale": "Satışı Tamamla",
        "payment_cash": "Nakit",
        "payment_card": "Kart",
        "total": "Toplam",
        "cashbox_screen": "Kasa",
"total_sales": "Toplam Satış",
"cash_total": "Nakit Toplamı",
"card_total": "Kart Toplamı",
"transaction_type": "İşlem Türü",
"amount": "Tutar",
"timestamp": "Zaman",
"close_day": "Günü Kapat",
"export_report": "Raporu Dışa Aktar",
"day_closed": "Gün Sonu",
"cashbox_closed_success": "Kasa başarıyla kapatıldı.",
"already_closed": "Bugün zaten kapatılmış.",
"report_exported": "Rapor başarıyla dışa aktarıldı."
    },
    "en": {
        "settings_screen": "Settings",
        "sales_screen": "Sales",
        "product_screen": "Products",
        "report_screen": "Reports",
        "dashboard_title": "CodexiaPOS Dashboard",
        "complete_sale": "Complete Sale",
        "payment_cash": "Cash",
        "payment_card": "Card",
        "total": "Total",
        "total_sales": "Total Sales",
  "cash_total": "Cash Total",
  "card_total": "Card Total",
  "transaction_type": "Transaction Type",
  "amount": "Amount",
  "timestamp": "Time",
  "close_day": "Close Day",
  "export_report": "Export Report",
  "day_closed": "Day Closure",
  "cashbox_closed_success": "Cashbox successfully closed.",
  "already_closed": "Already closed today.",
  "report_exported": "Report successfully exported."

    }
}

def set_language(lang):
    global LANG
    LANG = lang

def t(key):
    return translations.get(LANG, {}).get(key, key)