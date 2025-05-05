import string
import matplotlib.pyplot as plt


## Kod po edycji
def letter_histogram(text):
    alphabet = list(string.ascii_lowercase)
    letter_dict = {letter : 0 for letter in alphabet}
    for letter in alphabet:
        number_of_occurences = text.count(letter.lower())
        letter_dict[letter] = number_of_occurences
    x = list(letter_dict.keys())
    y = list(letter_dict.values())
    plt.bar(x, y)
    plt.title("Częstość wystąpień liter")
    plt.show()


if __name__ == "__main__":

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
    plt.bar(rysuj1[0:6], rysuj2[0:6])
    plt.show()

    ## Kod po edycji - wersja 2
    text = open("text.txt", "r").read()
    letter_histogram(text)

