def rozszyfruj():
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    text = input("Podaj tekst do rozszyfrowania : ")
    rozszyfrowany = ""

    for i in range(len(text)):
        for p in range(len(alfabet)):
            znaleziono = False
            if text[i] == alfabet[p]:
                x = alfabet[(p + 13) % 26]
                rozszyfrowany = rozszyfrowany+ x
                znaleziono = True
                break
            if text[i] == alfabet[p].upper():
                x = alfabet[(p + 13) % 26]
                rozszyfrowany = rozszyfrowany + x.upper()
                znaleziono = True
                break
        if not znaleziono:
            rozszyfrowany = rozszyfrowany + text[i]
    return rozszyfrowany


print(rozszyfruj())
