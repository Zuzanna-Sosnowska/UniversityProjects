import datetime
import os
import shutil
import time


def backup(dir_path, file_extention_list):
    """
    :param dir_path: Ścieżka do katalogu, w którym znajdują się pliki, których kopię zamierzamy utworzyć
    :param file_extention_list: Lista rozszerzeń plików
    :return: nowy folder Backupcopy-{aktualna data}, w którym znajdują się pliki edytowane w okresie krótszym niż 3 dni temu
    """
    # tworzymy katalog o nazwie Backup/copy_{dzisiejsza data}, o ile już nie istnieje
    if not os.path.isdir(f"C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_3\\Backup/copy_{datetime.date.today()}"):
        os.mkdir(f"C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_3\\Backupcopy-{datetime.date.today()}")

    # przechodzimy po każdym elemencie z katalogu o ścieżce zadanej jako argument
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # dla każdego pliku z katalogu sprawdzamy, czy posiada rozszerzenie z listy rozszerzeń zadanej jako argument
            for extention in file_extention_list:
                if file.endswith(extention):
                    # tworzymy całą ścieżkę do pliku
                    filepath = str(os.path.join(root, file))
                    # sprawdzamy datę ostatniej edycji pliku - od aktualnej daty w dniach odejmujemy datę
                    # ostatniej edycji w dniach
                    if (float(time.time())/(60*60*24)) - (float(os.path.getmtime(filepath))/(60*60*24)) <= 3:
                        shutil.copy2(filepath, f"C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_3\\Backupcopy-{datetime.date.today()}")


backup("C:\\Users\\Zuzia\\Desktop\\testowy", [".txt", ".jpg"])



