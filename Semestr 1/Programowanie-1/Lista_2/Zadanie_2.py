symbol = input("Symbol do wyszukania: ")
text = input("Wprowadź tekst: ")
len(text)
for i in range(len(text)):
    if symbol == text[i]:
        print("Symbol na pozycji: ", i)
        break  # Program wypisze nam tylko pierwszą pozycję, która będzie zgodna z symbolem.
        # bez "break" program wypisze wszystkie pozycje, na których pojawia się symbol.

