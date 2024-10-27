from zipfile import ZipFile
import datetime
import os


def save_as_zip(dir_path):
    """
    :param dir_path: ścieżka do katalogu
    :return: zip składający się z wszystkich folderów w katalogu
    """
    # tworzymy pustą listę na ścieżki do plików w katalogu
    file_paths = []

    # pętla przechodzi po każdym elemencie z katalogu
    for root, directories, files in os.walk(dir_path):
        for filename in files:
            # łączymy strumień z nazwą pliku, aby otrzymać pełną ścieżkę do pliku
            filepath = str(os.path.join(root, filename))
            # dodajemy ścieżkę do pliku do listy na ścieżki
            file_paths.append(filepath)

    # uzyskujemy nazwę katalogu ze ścieżki
    folder_name = dir_path.split('\\')[-1]
    with ZipFile(f"{datetime.date.today()}_{folder_name}.zip", 'w') as z:
        # zapisywanie wszystkich plików z katalogu do zipa
        for file_path in file_paths:
            split_path = file_path.split('\\')
            # uzyskujemy nazwy podkatalogów katalogu zadanego jako argument, do których zapisujemy pliki znajdujące się w podkatalogach
            arc_name = '\\'.join(split_path[split_path.index(folder_name):])
            z.write(file_path, arc_name)

save_as_zip("\\rakiety")
