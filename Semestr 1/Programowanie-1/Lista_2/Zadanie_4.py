symbol = input("Symbol do wyszukania: ")
text = input("Wprowadź tekst: ")
x = 0
for i in range(len(text)):
    if symbol == text[i]:
        x = x+1
print("Ilość symboli w tekście: ", x)