import requests
from bs4 import BeautifulSoup
import webbrowser


def page_from_wikipedia():
    while True:
        # otrzymujemy kod źródłowy artykułu z wikipedii
        url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        # uzyskujemy kod źródłowy w htmlu
        soup = BeautifulSoup(url.content, "html.parser")
        # funkcja ".find" szuka pierwszego elementu z atrybutem "class" zawierającym "firstHeading" (tytuł artykułu),
        # a następnie zamienia go na tekst
        title = soup.find(class_="firstHeading").text
        print(f"{title} \nCzy chcesz zobaczyć artukuł (T/N)")
        ans = input("").lower()
        if ans == "t":
            url = "https://en.wikipedia.org/wiki/%s" % title
            webbrowser.open(url)
            break
        elif ans == "n":
            print("Koniec!")
            break
        else:
            print("Zły wybór!")
            continue


page_from_wikipedia()
