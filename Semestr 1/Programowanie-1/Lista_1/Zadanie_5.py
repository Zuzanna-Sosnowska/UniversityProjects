minuty = int((2.5 * (6 * 60 + 15) + 4.8 * (4 * 60 + 12)) / 60)

godzina_powrotu = 6 + int((52 + minuty) / 60)
minuta_powrotu = int((52 + minuty) % 60)

print(f"Biegacz wróci o {godzina_powrotu} : {minuta_powrotu}")
