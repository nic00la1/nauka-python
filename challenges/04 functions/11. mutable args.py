# Przekazywanie mutowalnych danych do funkcji jak słownik, zadanie: 
# 1) Utwórz słownik opisujący pracownika i zapisz go w zmiennej
#    employee. Do elementów słownika dodaj: 
#    name, email, rank (stopień - wpisz programmer), salary (8000)
# 2) Napisz funkcje promoteToManager, która przyjmuje parametr
#    o nazwie user, gdzie przekazany będzie słownik.
# 3) Wewnątrz funkcji zmień wartości elementów przekazanego
#    słownika user, podnieś pensje o 50%, zmień rank
#    na manager. Dodatkowo sprawdź czy przypadkiem przekazany
#    pracownik już jest managerem, w takim wypadku podaj w konsoli,
#    że osoba ta już jest managerem i wyjdź z funkcji z return.
# 4) Wywołaj funkcję promoteToManager i przekaż utworzony na początku
#    słownik, pokaż w konsoli czy został on zaktualizowany.
#

employee = {
    "name": "Nicola",
    "email": "nicosia.k@Interia.pl",
    "rank": "Programmer",
    "salary": 8000
}

def promoteToManager(user):
    if user["rank"] == "manager":
        print(f"Pracownik {user["name"]} już jest managerem!")
        return
    else:
        user["rank"] = "manager"
        user["salary"] *= 1.5
        print(f"Awansowano pracownika {user["name"]} na rangę: // {user["rank"]} // --> Gratulację :) !")

print("Pracownik przed awansem: ")
print(employee)
promoteToManager(employee)
print("Pracownik po awansie: ")
print(employee)