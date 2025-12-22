# Zadanie: Tworzenie profilu użytkownika
#
# Cel: Napisz program, który umożliwia utworzenie profilu użytkownika w systemie.
# Program powinien prosić użytkownika o podanie imienia, nazwiska, wieku oraz
# miasta pochodzenia. Nie wszystkie informacje są wymagane. Użyj funkcji z nazwanymi
# argumentami.
# 
# Kroki do wykonania:
# 1) Zdefiniuj funkcję createUserProfile przyjmującą argumenty: firstName, lastName,
#    age oraz city
# 2) Funkcja powinna zwracać słownik zawierający informację o profilu użytkownika.
# 3) Poproś użytkownika o wprowadzenie wymaganych danych.
# 4) Wywołaj funkcję createUserProfile z odpowiednimi argumentami wprowadzonymi przez
#    użytkownika i przechowaj zwrócony słownik.
# 5) Wyświetl zwrócony profil użytkownika.
#
# Rozwiązanie

def createUserProfile(firstName, lastName, age, city):
    user = {
        "firstName": firstName,
        "lastName": lastName,
        "age": age,
        "city": city,
    }
    return user

firstName = input("Podaj imię: ")
lastName = input("Podaj nazwisko: ")
age = int(input("Podaj wiek: "))
city = input("Podaj miasto: ")

userProfile = createUserProfile(firstName=firstName, lastName=lastName, age=age, city=city)

print("\n===PROFIL UŻYTKOWNIKA ===")
print("Imię:", userProfile["firstName"])
print("Nazwisko:", userProfile["lastName"])
print("Wiek:", userProfile["age"])
print("Miasto:", userProfile["city"])