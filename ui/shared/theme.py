from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication
import os
from config.settings import DEFAULT_THEME

def apply_theme(app: QApplication, theme_name: str):

    """
    Uygulamanın genel stilini uygular:
    - Büyük fontlar (başlangıç ekranı için)
    - Buton boşlukları ve padding
    - Modern Windows/macOS benzeri görünüm
    """

    # Genel font ayarı
    app.setFont(QFont("Segoe UI", 11))  # Windows/macOS için modern font
    qss_path = os.path.join("assets", "styles", f"{theme_name}.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
        print(f"Tema yüklendi: {theme_name}")
    else:
        print(f"Uyarı: {qss_path} bulunamadı, varsayılan stil kullanılacak.")
        app.setStyleSheet("")  # Qt varsayılanına dön

    # QSS (Qt StyleSheet) ile stil
    style = """
    QWidget {
        background-color: #f3f3f3;
        font-family: 'Segoe UI';
        font-size: 14px;
    }

    QLabel#LoginTitle {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #2b2b2b;
    }

    QLineEdit {
        padding: 8px 10px;
        margin: 5px 0;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
    }

    QPushButton {
        background-color: #0078d7;
        color: white;
        border-radius: 6px;
        padding: 10px 20px;
        margin-top: 15px;
        font-size: 14px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #005a9e;
    }

    QPushButton:pressed {
        background-color: #004578;
    }
"""

    app.setStyleSheet(style)