import random
import string


def create_password(k=8, numb_of_upper: int = 1, numb_of_symbols: int = 1):
    """
    :param k: długość hasła
    :param numb_of_upper: ilość wielkich liter w haśle
    :param numb_of_symbols: ilość symboli w haśle
    :return: hasło długości k
    """
    if numb_of_upper + numb_of_symbols > k:
        return ValueError
    # Program zwróci błąd, jeśli suma znaków specjalnych i wielkich liter przekroczy możliwą długość hasł
    s1 = list(string.ascii_lowercase) # lista małych liter
    s2 = list(string.ascii_uppercase) # lista wielkich liter
    s3 = list(string.digits) # lista cyfr
    s4 = list(string.punctuation) # lista znaków specjalnych
    s5 = s3 + s4 # lista cyfr i znaków specjalnych
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s5)
    # tworzymy pustą listę na hasło
    password = []
    for i in range(numb_of_upper):
        # dodajemy do hasła wielkie litery
        password.append(s2[i])
    for i in range(numb_of_symbols):
        # dodajemy symbole do hasła
        password.append(s5[i])
    for i in range(k - (numb_of_upper + numb_of_symbols)):
        # dodajemy małe litery do hasła
        password.append(s1[i])
    # ustawiamy litery i znaki specjalne w dowolnej kolejności
    random.shuffle(password)
    return ''.join(password)



if __name__ == "__main__":
    print(create_password(8, 1, 1, ))
