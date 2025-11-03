import os

# === Genel Uygulama Ayarları ===
APP_NAME = "CodexiaPOS"
VERSION = "1.0.0"

# === Veritabanı Ayarları ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLES_DIR = os.path.join(BASE_DIR, "assets", "styles")
DB_NAME = "codexia.db"
DB_PATH = os.path.join(BASE_DIR, DB_NAME)

# === Tema Ayarları ===
DEFAULT_THEME = "dark"   # "dark" veya "light"
AUTO_NIGHT_LIGHT = False

# === Dil Ayarları ===
DEFAULT_LANGUAGE = "tr"

# === Pencere Boyutu ===
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

# === Yedekleme Ayarları ===
BACKUP_DIR = os.path.join(BASE_DIR, "backup")
os.makedirs(BACKUP_DIR, exist_ok=True)

# === Barkod Kayıt Klasörü ===
BARCODE_DIR = os.path.join(BASE_DIR, "assets", "barcodes")
os.makedirs(BARCODE_DIR, exist_ok=True)

# === Log Ayarları ===
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "access.log")