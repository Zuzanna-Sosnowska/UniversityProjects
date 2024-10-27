symbol = input("Symbol do wyszukania: ")
text = input("Wprowadź tekst: ")
x = int(input("Zaczynamy od pozycji: "))
for i in range(x, len(text)):
    if symbol == text[i]:
        print("Symbol na pozycji: ", i)
