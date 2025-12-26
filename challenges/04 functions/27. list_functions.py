# Zadanie - organizacja imprezy
# W tym zadaniu skorzystasz z operacji na listach do zorganizowania listy gości
# oraz listy potraw na imprezie. Nauczysz się dodawać, usuwać elementy,
# sortować listy oraz wykonywać inne podstawowe operacje.
# 
# 1) Stwórz listę `guests` z pięcioma imionami gości.
# 2) Wyświetl długość listy gości, aby sprawdzić, ilu masz gości.
# 3) Dodaj jeszcze dwóch gości na koniec listy.
# 4) Jeden z gości nie może przyjść. Usuń go z listy.
# 5) Posortuj listę gości alfabetycznie i wyświetl ją.
# 6) Stwórz listę `dishes` z trzema potrawami.
# 7) Dodaj do listy potraw jeszcze dwie nowe potrawy.
# 8) Wyświetl potrawę, która znajduje się na środku listy.
# 9) Usuń ostatnią potrawę z listy.
# 10) Sprawdź, czy na liście potraw znajduje się 'Pizza'. Jeśli tak,
#    wyświetl komunikat "Pizza jest na liście!", w przeciwnym razie
#    dodaj Pizzę do listy potraw.

guests = ["Monika", "Mariusz", "Jarosław", "Wiktor", "Amelia"]
print(guests)
print("Masz", len(guests), "gości.")

guests.extend(["Wiola", "Joanna"])
print(guests)
print("Masz", len(guests), "gości.")

guests.remove("Wiktor")
print("Gość Wiktor nie może przyjść! - Usunięto go z listy.")

guests.sort()
print("Posortowana lista gości:", guests)

dishes = ["Zupa Grzybowa", "Karp", "Kotlet Devolay"]
dishes.extend(["Pierogi", "Rosół"])

print(dishes)

middleDish = dishes[len(dishes) // 2]
print(middleDish)

dishes.pop()
print("Potrawy po usunięciu ostatniej:", dishes)

if "Pizza" in dishes:
    print("Pizza jest na liście!")
else:
    dishes.append("Pizza")
    print("Dodano Pizzę do listy dań!")