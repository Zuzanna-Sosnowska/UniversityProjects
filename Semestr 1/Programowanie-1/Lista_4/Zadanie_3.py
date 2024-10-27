def zaszyfruj():
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    text = input("Wprowadź tekst do zaszyfrowania : ")
    zaszyfrowany = ""

    for i in range(len(text)):
        for p in range(len(alfabet)):
            znaleziono = False
            if text[i] == alfabet[p]:
                x = alfabet[(p+13) % 26]
                zaszyfrowany = zaszyfrowany + x
                znaleziono = True
                break
            if text[i] == alfabet[p].upper():
                x = alfabet[(p+13) % 26]
                zaszyfrowany = zaszyfrowany + x.upper()
                znaleziono = True
                break
        if not znaleziono:
            zaszyfrowany = zaszyfrowany +text[i]
    return zaszyfrowany

print(zaszyfruj())