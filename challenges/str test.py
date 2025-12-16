# 1. Wykorzystaj funkcję input() wbudowaną w python do
#    pobrania informacji od użytkownika z konsoli.
#    Poproś użytkownika o podanie imienia, nazwiska, miasta
#    Zapisz te informacje w zmiennych name, surname i city
# 2. Wyświetl w konsoli tekst podsumowujący pobrane dane: 
#    "Nazywasz się Ania kowalska i mieszkasz: Krk"

print("=== Podaj informację o sobie ===")

print("Wpisz imię: ")
name = input()
print("Wpisz nazwisko: ")
surname = input()
print("Wpisz miasto: ")
city = input()

print("Nazywasz się " + name + " " + surname + " i mieszkasz w: " + city)