# Zadanie: Zarządzanie stanem konta użytkownika
#
# Cel: Napisz program do zarządzania stanem konta użytkownika, który pozwala na
# dodawanie i usuwanie środków oraz wyświetlanie aktualnego stanu konta. Program
# powinien korzystać z globalnej zmiennej do przechowywania stanu konta oraz
# zawierać funkcje do modyfikacji tego stanu i wyświetlania go.
#
# Kroki do wykonania:
# 1) Zdefiniuj globalną zmienną accountBalance z wartością początkową 0 
# 2) Napisz funkcję addFunds, która przyjmuje kwotę do dodania do konta.
#    Funkcja ta powinna modyfikować globalną zmienną accountBalance.
# 3) Napisz funkcję withdrawFunds, która przyjmuje kwotę do wypłaty z konta.
#    Sprawdź, czy stan konta pozwala na wypłatę - jeśli nie, wyświetl odpowiedni komunikat.
# 4) Napisz funkcję displayBalance, która wyświetla aktualny stan konta.
# 5) Zapytaj użytkownika w pętli o działanie (dodanie środków, wypłata, wyświetlenie stanu)
#    i odpowiednio zareaguj, wywołując odpowiednią funkcję
#
# Rozwiązanie:

accountBalance = 0

def addFunds(amount):
    global accountBalance
    accountBalance += amount
    print(f"Dodano sumę! {accountBalance - amount} + {amount} = {accountBalance}")
    return sum

def withdrawFunds(amount):
    global accountBalance

    if accountBalance >= amount and accountBalance > 0:
        accountBalance -= amount # odejmowanie
        print(f"Wypłacono kwotę: {accountBalance + amount} - {amount} = {accountBalance}")
    else:
        print("Nie możesz wypłacić! Nie masz tyle środków na końcie")

def displayBalance():
    global accountBalance

    print("Twój aktulany stan konta wynosi:", accountBalance)

# 5) Zapytaj użytkownika w pętli o działanie (dodanie środków, wypłata, wyświetlenie stanu)
#    i odpowiednio zareaguj, wywołując odpowiednią funkcję

while True:
    option = int(input("Jakie działanie chcesz wykonać? (1. dodanie środków, 2. wypłata, 3. wyświetlenie stanu, 4. koniec): "))

    if option == 1:
        print("Dodawanie środków na konto: ")
        amount = int(input("Wprowadź ilość wpłacanej kwoty: "))
        addFunds(amount)
    elif option == 2:
        print("Wypłacanie środków z konta: ")
        amount = int(input("Wprowadź ilość wypłacanej kwoty: "))
        withdrawFunds(amount)
    elif option == 3:
        displayBalance()
    elif option == 4:
        break
    else:
        print("Nie istnieje taka opcja! Spróbuj ponownie")