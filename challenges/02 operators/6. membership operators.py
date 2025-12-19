# Zadanie do wykonania: 
# Wykorzystaj operatory przynależności (in, not in) do sprawdzenia
# obecności elementów w kolekcjach i użycie instrukcji warunkowej if.
# 1) Sprawdź, czy liczba 7 znajduje się w liście 'numbers' i wyświetl odpowiedni komunikat.
# 2) Sprawdź, czy ciąg znaków "kot" nie znajduje się w tuple 'animals' i wyświetl odpowiedni komunikat.
# 3) Stwórz słownik 'user' z kluczami 'name' i 'age'. Sprawdź, czy klucz 'name' znajduje się w słowniku.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if 7 in numbers:
    print("7 w liście")
else:
    print("7 nie jest w liście")

animals = ("lew", "kot", "niedźwiedź", "żyrafa", "koń", "foka", "tygrys", "gepard")

if "kot" not in animals:
    print("kot nie jest w krotce")
else:
    print("kot jest w krotce")

user = {
    "name": "Nicola",
    "age": 19
}

if "name" in user:
    print("Klucz 'name' znajduje się w słowniku.")
else: 
    print("Klucza nie ma.")