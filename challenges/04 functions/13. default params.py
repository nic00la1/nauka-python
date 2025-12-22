# 
# Funkcja z domyślnymi wartościami parametrów
# 1) Napisz funkcję z parametrami: 
#    - email
#    - country z domyślną wartością "Polska"
#    - company z domyślną wartością "Example Ltd"
# 2) Zwróć z funkcji słownik z elementami jak parametry
# 3) Przetestuj funkcję z jednym argumentem ola@example.com
#    oraz drugi przypadek z kasia@example.com będąca z UK

def getPerson(email, country="Polska", company = "Example Ltd"):

    person = {
        "email": email,
        "country": country,
        "company": company
    }

    print(person)
    return person 

getPerson("ola@example.com")
getPerson("kasia@example.com", "UK")
getPerson("adam@example.com", "DE", "Volkswagen")