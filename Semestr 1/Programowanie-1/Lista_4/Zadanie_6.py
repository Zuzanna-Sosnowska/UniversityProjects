a = 5

row = [0 for i in range(a + 2)]
row[1] = 1

for i in range(1, a+2):
    print("\n", ' ' * (a - i + 3), end="")
    print()
    old = 0
    for j in range(1, a + 2):
        if row[j] != 0:
            print(f"{row[j]:2} ", end="")
            tmp = row[j]
            row[j] = row[j] + old
            old = tmp
        else:
            tmp = row[j]
            row[j] = row[j] + old
            old = tmp
            break
