from PyQt6.QtWidgets import (
    QWidget, QLabel, QComboBox, QVBoxLayout, QPushButton,
    QCheckBox, QSpinBox, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont
from ui.shared.language import t

class SettingsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(t("settings_screen"))
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Başlık
        self.title = QLabel(t("settings_screen"))
        self.title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        self.title.setObjectName("SettingsTitle")
        self.back_btn = QPushButton(t("back"))
        # Dil seçimi
        self.language_label = QLabel("Dil Seçimi")  # ✅ eksik olan satır
        self.language_select = QComboBox()
        self.language_select.addItem("Türkçe", "tr")
        self.language_select.addItem("English", "en")

        # Tema seçimi
        self.theme_label = QLabel("Tema")
        self.theme_select = QComboBox()
        self.theme_select.addItems(["light", "dark"])

        # Otomatik night light
        self.night_light_checkbox = QCheckBox("Otomatik Night Light (20:00 - 06:00)")
        
        # Pencere boyutu
        self.window_size_label = QLabel("Pencere Boyutu (Genişlik x Yükseklik)")
        self.width_input = QSpinBox()
        self.width_input.setRange(600, 1920)
        self.width_input.setValue(1024)

        self.height_input = QSpinBox()
        self.height_input.setRange(400, 1080)
        self.height_input.setValue(768)

        size_layout = QHBoxLayout()
        size_layout.addWidget(self.width_input)
        size_layout.addWidget(self.height_input)

        # Kaydet butonu
        self.save_btn = QPushButton("Kaydet")

        # Üst boşluk
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Ayarlar
        layout.addWidget(self.title)
        layout.addWidget(self.language_label)
        layout.addWidget(self.language_select)
        layout.addWidget(self.theme_label)
        layout.addWidget(self.theme_select)
        layout.addWidget(self.night_light_checkbox)
        layout.addWidget(self.window_size_label)
        layout.addLayout(size_layout)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.back_btn) # Geri tuşunu da ekleyelim
        # Alt boşluk
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Margin ve spacing
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(15)

        self.setLayout(layout)