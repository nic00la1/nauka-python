# 1. Stwórz krotkę z wartościami: 50, 100, 150, 200, 250
# 2. Pokaż typ krotki w konsoli
# 3. Pokaż w konsoli ilość elementów krotki
# 4. Pokaż ostatni element krotki wykorzystując len() -1
# 5. Następnie pokaż elementy od drugiego do czwartego
# 6. Pokaż trzeci element od końca z ujemnym indeksem

data = (50, 100, 150, 200, 250)

print("1. Typ krotki: ", type(data))
print("2. Ilość elementów krotki: ", len(data))

print("3. Ostatni element krotki: ", data[len(data) - 1])

print("4. Elementy od drugiego do czwartego: ", data[1:4])
print("5. Trzeci element od końca z ujemnym indeksem: ", data[-3])

