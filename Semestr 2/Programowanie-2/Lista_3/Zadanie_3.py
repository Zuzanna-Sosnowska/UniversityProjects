from pypdf import PdfMerger


def all_to_pdf(list_of_pdf, new_name):
    """
    :param list_of_pdf: Lista, zawieracjąca ścieżki do plików pdf w odpowiedniej kolejności
    :param new_name: Nowa nazwa pliku, w którym znajdował się będzie nowy pdf
    :return: Nowy plik pdf, składający się z zadanych plików pdf w odpowiedniej kolejności
    """
    # Korzystamy z funkcji z biblioteki pypdf, która łączy ze sobą pliki pdf i wpętli dodajemy pliki do zmiennej merger
    merger = PdfMerger()
    for files in list_of_pdf:
        merger.append(files)

    # zapisujemy pliki pod nazwą zadaną jako parametr
    merger.write(f"{new_name}.pdf")
    merger.close()


all_to_pdf(["C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_2\\file3.pdf",
            "C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_2\\file2.pdf",
            "C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_2\\file3.pdf"], 'number_one')
