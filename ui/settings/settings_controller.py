from ui.shared.language import set_language, t
from config import settings
from ui.shared.theme import apply_theme
from PyQt6.QtWidgets import QApplication

class SettingsController:
    def __init__(self, view, refresh_callback, app_window,return_callback):
        self.view = view
        self.refresh_callback = refresh_callback
        self.app_window = app_window
        self.return_callback=return_callback

        # Varsayılan değerleri yükle
        self.view.language_select.setCurrentText(settings.DEFAULT_LANGUAGE)
        self.view.theme_select.setCurrentText(settings.DEFAULT_THEME)
        self.view.night_light_checkbox.setChecked(settings.AUTO_NIGHT_LIGHT)
        self.view.width_input.setValue(settings.WINDOW_WIDTH)
        self.view.height_input.setValue(settings.WINDOW_HEIGHT)

        self.view.save_btn.clicked.connect(self.apply_settings)
        self.view.back_btn.clicked.connect(self.return_callback)  # ❌ ama back_btn yoksa hata verir
 
    def apply_settings(self):
        print("Aktif stil:", QApplication.instance().styleSheet())
        
        # 1. Dil seçimi
        lang_code = self.view.language_select.currentText()  # ✅ currentText kullan
        set_language(lang_code)
        settings.DEFAULT_LANGUAGE = lang_code

        # 2. Tema seçimi
        theme = self.view.theme_select.currentText()
        apply_theme(QApplication.instance(), theme)
        settings.DEFAULT_THEME = theme

        # 3. Night light
        settings.AUTO_NIGHT_LIGHT = self.view.night_light_checkbox.isChecked()

        # 4. Pencere boyutu
        w = self.view.width_input.value()
        h = self.view.height_input.value()
        settings.WINDOW_WIDTH = w
        settings.WINDOW_HEIGHT = h
        self.app_window.resize(w, h)

        print(f"Ayarlar güncellendi → Dil: {lang_code}, Tema: {theme}, "
            f"NightLight: {settings.AUTO_NIGHT_LIGHT}, Boyut: {w}x{h}")
        apply_theme(QApplication.instance(), theme)
        # 5. UI’yi güncelle ve dashboard’a dön
        self.refresh_callback()
        self.app_window.show_dashboard()