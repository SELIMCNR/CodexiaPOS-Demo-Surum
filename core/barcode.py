
import os
import barcode
from barcode.writer import ImageWriter

def generate_barcode(code, filename):
    # Klasör yoksa oluştur
    os.makedirs("assets/barcodes", exist_ok=True)

    # Dosya yolunu uzantısız veriyoruz
    filepath = os.path.join("assets/barcodes", filename)

    # EAN13 barkod nesnesi oluştur
    ean = barcode.get('ean13', code, writer=ImageWriter())

    # Kaydet → otomatik .png ekler
    ean.save(filepath)

    # 13 haneli tam kodu döndür
    return ean.get_fullcode(), filepath + ".png"
import cv2
from pyzbar.pyzbar import decode

def scan_barcode_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        for barcode in decode(frame):
            code = barcode.data.decode('utf-8')
            print("Barkod:", code)
            cap.release()
            return code
        cv2.imshow('Barkod Okuyucu', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    