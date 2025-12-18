# Zadanie do wykonania: 
# 1. Stwórz listę 'numbers' zawierającą liczby od 7 do 12.
#    Wyświetl tę listę.
# 2. Zamień listę 'numbers' na krotkę 'tupleNumbers' i 
#    wyświetl wynik.
# 3. Utwórz listę 'mixedList' składającą się z różnych typów
#    danych, np. string, liczba całkowita, liczba zmiennoprzecinkowa.
#    Wyświetl 'mixedList'. 
# 4. Przekształć 'mixedList' w zbiór 'setMixed' i wyświetl jego
#    typ oraz zawartość.
# 5. Zamień 'tupleNumbers' na zamrożony zbiór 'frozenSetNumbers'
#    i wyświetl jego typ oraz zawartość.
# 6. Stwórz krotkę 'nameAgePairs' zawierającą pary (imię, wiek),
#    a następnie na jej podstawie utwórz słownik 'ageDict'.
#    Wyświetl słownik, a potem wyświetl wiek osoby o imieniu 'Marek'.

numbers = [7, 8, 9, 10, 11, 12]
print(numbers)

tupleNumbers = tuple(numbers)
print(tupleNumbers)

mixedList = ["Nicola", 77, 92.2]
print(mixedList)

setMixed = set(mixedList)
print("Typ zbioru setMixed:", type(setMixed), "Zawartość:", setMixed)

frozenSetNumbers = frozenset(tupleNumbers)
print("Typ zbioru frozenSetNumbers:", type(frozenSetNumbers), "Zawartość:", frozenSetNumbers)

nameAgePairs = (("Marek", 30), ("Marzena", 25))
ageDict = dict(nameAgePairs)

print("Wiek osoby o imieniu Marek:", ageDict["Marek"])