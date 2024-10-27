import qrcode
import cv2


def create_qr(sentence, file_name):
    """
    :param sentence: Treść, którą ma być kod QR
    :param file_name: Nazwa nowego pliku
    :return: Plik, w postaci kodu QR
    """
    # korzystając z funkcji z biblioteki qrcode tworzymy kod QR
    image = qrcode.make(sentence)
    # zapisujemy kod QR jako obraz o rozszerzeniu '.png'
    image.save(f'{file_name}.png')


def read_qr_code(file_path):
    """
    :param file_path: Ścieżka do pliku z kodem QR
    :return: treść zawartą w kodzie QR
    """
    # wczytujemy obraz ze ścieżki do pliku
    img = cv2.imread(file_path)
    # wykrywamy kod QR na obrazku
    detect = cv2.QRCodeDetector()
    # rozszyfrowujemy treść zawartą w kodzie QR
    value, points, straight_qrcode = detect.detectAndDecode(img)
    # zwracamy treść zawartą pod kodem QR
    return value


create_qr('Oto mój pierwszy kod qr!!', 'first_qr')

# create_qr("hello world!", 'C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_3\\hello_world')
print(read_qr_code('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_3\\first_qr.png'))
