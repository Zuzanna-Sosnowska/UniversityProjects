def unix_to_dos(path_to_file):
    """
    :param path_to_file: Scieżka do pliku
    :return: Plik z Windowsowymi znakani końca linii
    """
    # definiujemy znaki końca linii
    windows_line_ending = b'\r\n'
    unix_line_ending = b'\n'
    # otwieramy plik ze ścieżki. 'rb' to uprawnienia, które nadajemy plikowi, z ang. "read"
    with open(path_to_file, 'rb') as f:
        contents = f.read()
        # korzystając z funkcji wbudowanej zamieniamy znaki konca linii z unixsowych na windowsowe
        content = contents.replace(unix_line_ending, windows_line_ending)
    # zapisujemy edytowany plik. 'wb' to uprawnienia, które nadajemy przy zapisywaniu, z ang. "write"
    with open(path_to_file, 'wb') as open_file:
        open_file.write(content)


def dos_to_unix(path_to_file):
    unix_line_ending = b'\n'
    windows_line_ending = b'\r\n'
    with open(path_to_file, 'rb') as f:
        contents = f.read()
        content = contents.replace(windows_line_ending, unix_line_ending)
    with open(path_to_file, 'wb') as open_file:
        open_file.write(content)


dos_to_unix("C:\\Users\\Zuzia\\Desktop\\testowy\\pliczek.txt")
# unix_to_dos("C:\\Users\\Zuzia\\Desktop\\testowy\\pliczek.txt")
