import string
import matplotlib.pyplot as plt

alfabet = list(string.ascii_lowercase)
licznik = [0 for i in range(len(alfabet))]
slownik = dict(zip(alfabet, licznik))

slowo = 'Ala ma kota'

for znak in alfabet:
    licz_tmp = slowo.lower().count(znak.lower())
    slownik[znak.lower()] = licz_tmp

slownik = {k: v for k, v in sorted(slownik.items(), key=lambda item: item[1], reverse=True)}
print(slownik)
rysuj1 = list(slownik.keys())
rysuj2 = list(slownik.values())
plt.bar(rysuj1[0:10], rysuj2[0:10])
plt.show()

