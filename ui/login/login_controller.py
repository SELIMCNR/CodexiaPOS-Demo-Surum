from core.security import verify_password
from models.user_model import get_user_by_username

class LoginController:
    def __init__(self, view, on_success=None):
        self.view = view
        self.on_success = on_success
        self.view.login_btn.clicked.connect(self.handle_login)

    def handle_login(self):
        # LoginView'deki doğru alan isimleri
        username = self.view.username_input.text()
        password = self.view.password_input.text()

        user = get_user_by_username(username)

        if user and verify_password(password, user["hashed_password"]):
            print("Giriş başarılı")
            if self.on_success:
                self.on_success(user)  # Dashboard’a yönlendir
        else:
            print("Hatalı giriş")
            # İstersen burada kullanıcıya mesaj kutusu da gösterebilirsin
            # örn: QMessageBox.warning(self.view, "Hata", "Kullanıcı adı veya şifre yanlış")