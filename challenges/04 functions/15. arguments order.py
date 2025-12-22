# Zadanie: Rezerwacja biletów na koncert 
# 
# Cel: Napisz program, który pozwoli użytkownikowi zarezerwować bilety na koncert.
# 
# Kroki do wykonania:
# 1) Zdefiniuj funkcję bookTickets, która przyjmuje nazwę zespołu jako argument
#    pozycyjny (band), liczbę biletów jako argument pozycyjny, a rodzaj biletów i sekcję
#    jako argumenty nazwane z domyślnymi wartościami jako standard i general
# 2) Funkcja powinna wyświetlać informacje o rezerwacji, włączając w to wszystkie
#    podane detale.
# 3) Poproś użytkownika o wprowadzenie nazwy zespołu i liczby biletów,
#    następnie tylko je przekaż przy wywołaniu funkcji.
#

def bookTickets(band, tickets, / , *, typeOfTickets="standard", section="general"):
    print("=== Rezerwacja biletów ===")
    print("Zespół:", band)
    print("Liczba biletów:", tickets)
    print("Rodzaj biletów:", typeOfTickets)
    print("Sekcja:", section)

band = input("Wprowadź nazwę zespołu: ")
tickets = int(input("Wprowadź ilość biletów: "))
bookTickets(band, tickets)