# Zadanie do wykonania: 
# Wykorzystaj instrukcje warunkowe do stworzenia prostego programu
# decyzyjnego, analizując wartość zmiennej 'number'.
# 1) Stwórz zmienną 'number' i przypisz jej wartość 15.
# 2) Sprawdź, czy 'number' jest większe od 10. Jeśli tak, wyświetl komunikat.
# 3) Sprawdź, czy 'number' jest równe 15. Jeśli tak, wyświetl komunikat.
# 4) Użyj `elif` do sprawdzenia, czy 'number' jest równe 20, 25, lub większe od 30.
#    Dla każdego przypadku wyświetl odpowiedni komunikat.
# 5) Jeśli żaden z powyższych warunków nie jest spełniony, użyj `else` do wyświetlenia
#    domyślnego komunikatu.
# 6) Dodaj zagnieżdżoną instrukcję warunkową, aby sprawdzić dodatkowy warunek
#    dla jednego z przypadków.

number = 15

if number > 10:
    print("Number jest większy od 10")

if number == 15:
    print("Number jest równe 15")
elif number == 20:
    print("Number jest 20")
elif number == 25:
    print("Number jest 25")
elif number > 30:
    print("Number jest większy od 30")
else:
    print("Domyślny komunikat.")


if number > 10: 
    print("Number jest większy niż 10")
    if number % 3 == 0:
        print("Number podzielny przez 3")