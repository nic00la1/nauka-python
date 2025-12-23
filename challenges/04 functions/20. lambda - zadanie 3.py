# Zadanie: Przetwarzanie danych użytkowników
# Cel: Napisz program do przetwarzania danych użytkowników z listy.
# 
# Kroki do wykonania:
# 1) Stwórz listę słowników users, gdzie każdy słownik zawiera klucze 'name' i 'age'
#    z przykładowymi danymi użytkownika.
# 2) Użyj filter do wyfiltrowania użytkowników, którzy mają więcej niż 18 lat.
# 3) Użyj map do podwojenia wieku przefiltrowanych użytkowników.
# 4) Użyj reduce do zsumowania wszystkich lat po przetworzeniu.
# 5) Wyświetl sumę lat przefiltrowanych i przetworzonych użytkowników.
#
# Rozwiązanie:

from functools import reduce

users = [
    {"name": "Jan", "age": 37},
    {"name": "Piotr", "age": 54},
    {"name": "Mariola", "age": 17},
    {"name": "Jarosław", "age": 68},
    {"name": "Mikołaj", "age": 15},
]

adults = list(filter(lambda user: user["age"] > 18, users))
print("Użytkownicy, którzy mają więcej niż 18 lat:", adults)

doubleAge = list(map(lambda user: user["age"] * 2, adults))
print("Podwojony wiek użytkowników pełnoletnich:", doubleAge)

totalAge = reduce(lambda x, y: x + y, doubleAge)
print("Suma lat przefiltrowanych i przetworzonych użytkowników:", totalAge)