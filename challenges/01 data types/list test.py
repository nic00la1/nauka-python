# 1. Stwórz listę data z kolejnymi liczbami: od 0 do 6.
# 2. Pokaż w konsoli długość listy, skasuj 2 element
#    i pokaż długość listy ponownie.
# 3. Użyj instrukcji warunkowej if z in do sprawdzenia czy 
#    liczba 3 jest w liście data, pokaż informację 
#    w konsoli, jeśli zachodzi taka sytuacja. Przykład: 
#    if 100 in someList:
#       print("100 jest w liście")
# 4. Użyj pętli for aby pokazać wartości w liście.
#    for el in someList:
#       print(f"Element listy z dodaną wartością 2: {el + 2})
# 5. Użyj pętli for, aby przejść po elementach listy, ale
#    pokaż ich wartości pomnożone przez 2.

data = [0, 1, 2, 3, 4, 5, 6]

print("Długość listy data: ", len(data))

del data[1]
print("Długość listy data, po usunięciu 2 elementu: ", len(data))

if 3 in data:
    print("Liczba 3 znajduje się w liście!")
else: 
    print("Liczba 3 nie znajduje się w liście.")

print("Wartości z listy data: ")
for el in data:
    print(el)

print("Wartości z listy data, pomnożone przez 2: ")
for el in data:
    newEl = el * 2
    print(newEl)