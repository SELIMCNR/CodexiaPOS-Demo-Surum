from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy

class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Ekranı")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Başlık
        self.title = QLabel("CodexiaPOS")
        self.title.setObjectName("LoginTitle")

        # Kullanıcı adı
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Kullanıcı Adı")

        # Şifre
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Spacer (üst ve alt boşluk için)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        layout.addWidget(self.title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)

        # Login butonu
        self.login_btn = QPushButton("Giriş Yap")
        layout.addWidget(self.login_btn)

        # Alt boşluk için spacer
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Margin ve spacing ayarları
        layout.setContentsMargins(40, 40, 40, 40)  # kenar boşlukları
        layout.setSpacing(15)  # widgetlar arası boşluk

        self.setLayout(layout)