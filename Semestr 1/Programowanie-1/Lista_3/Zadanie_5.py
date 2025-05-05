
def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)


def list_nwd(lista):
    result = lista[0]
    for i in range(1, len(lista)):
        result = nwd(result, lista[i])
    return result


ls = [i for i in range(1, 1000) if i % 13 == 0]
"""
Przykładowa lista liczb do tysiąca, które są podzielne przez 13. 
Używając komendy input można umożliwić użytkownikowi możliwość wprowadzenia własnej listy liczb.
"""
n = list_nwd(ls)
print(n)
