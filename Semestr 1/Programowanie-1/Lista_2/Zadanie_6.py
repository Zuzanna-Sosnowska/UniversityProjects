import math

x = input("Wprowadź tekst: ")
y = input("Wprowadź tekst: ")
len(x)
len(y)
p = min(len(x), len(y))
for i in range(p):
    if x[i] == y[i]:
        print("Symbol na pozycji ", i ,"zgodny")
    else:
        print("Symbol na pozycji ", i ,"niezgodny")
