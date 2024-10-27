from PyPDF2 import PdfWriter, PdfReader


def split_pdf(pdf_path, split_table):
    """
    :param pdf_path: ścieżka do pliku pdf
    :param split_table: lista z podziałem stron, wskazująca na ile stron po kolei dzielić pdf
    :return: pliki pdf o zadanej liczbie stron
    """
    reader = PdfReader(pdf_path)
    # obliczamy liczbę stron pliku pdf
    total_pages = len(reader.pages)
    # indeks aktualnej strony
    current_pages = 0
    # indeks wyjściowego pliku pdf
    file_idx = 1

    # pętla przechodząca przez każdy element z listy split_table
    for page_amount in split_table:
        output = PdfWriter()
        # pętla dla zadanej liczby stron dodaje je do końcowego pdfa
        for i in range(page_amount):
            # dodawanie strony do jednego z pdfów
            output.add_page(reader.pages[current_pages])
            # przesuwamy indeks strony
            current_pages += 1
            # jeśli użytkownik zażąda, aby plik pdf podzielić na więcej pdfów niż jest to możliwe, to program wyjdzie z pętli
            if current_pages >= total_pages:
                break
        # zapisujemy pliki do pdfa o nazwie file.{file_idx}, gdzie {file_idx} oznacza numer nowo utworzonego pdfa
        with open(f"file{file_idx}.pdf", "wb") as output_stream:
            output.write(output_stream)

        file_idx += 1

split_pdf('02680_gis_geo_swiat_fiz_fr.pdf', [2, 3, 6])
