# 
# Funkcje String:
# 1) Napisz funkcję getUserInformation z trzema parametrami:
#    name, surname, job
# 2) W getUserInformation zmień imię i nazwisko na duże litery,
#    zawód na małe, dodatkowo wyczyść te wartości
# 3) Połącz imię i nazwisko wraz z innym tekstem, aby uzyskać tekst, np.
#    "imię: MAŁGORZATA", nazwisko "STOKROTKA", zawód: testerka"
# 4) Zwróć powstały tekst z funkcji
# 5) Wywołaj funkcję getUserInformation na następujących
#    danych i pokaż wynik w konsoli:
#    - Małgorzata, Stokrotka, Testerka
#    - Daniel, Lis, Administrator
#

def getUserInformation(name, surname, job):
    name = name.upper()
    surname = surname.upper()
    job = job.lower()

    text = "imię: " + name + ", nazwisko: " + surname +", zawód: " + job 
    print(text)
    return text

getUserInformation("Małgorzata", "Stokrotka", "Testerka")
getUserInformation("Daniel", "Lis", "Administrator")