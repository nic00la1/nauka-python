# Zadanie z listą liczb od -4 do 4
# 1) Wyświetl w konsoli następujące informacje z użyciem pętli na liście
#    oraz instrukcji if elif else w celu sprawdzenia czy liczba jest parzysta
#    czy nie parzysta, oczywiście dodaj informację w konsoli
# 2) Pamiętaj, że 0 będzie oddzielnym przypadkiem, który musisz sprawdzić jako
#    pierwszy w if i w jej bloku napisz w konsoli tekst: "Zero jest parzyste".
#    Następnie w elif sprawdź, czy liczba jest parzysta, a oczywiście w else
#    będzie pewność, że jest nieparzysta.

numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

for num in numbers:
    if num == 0:
        print("Zero jest parzyste")
    elif num % 2 == 0:
        print(num, "jest parzysta")
    else:
        print(num, "jest nieparzysta")