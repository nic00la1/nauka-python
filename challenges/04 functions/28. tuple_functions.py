# Zdanie - Analiza danych demograficznych
# W tym zadaniu wykorzystasz krotki do przechowywania i analizy
# danych demograficznych. Użyj podstawowych operacji na krotkach
# do manipulacji danymi oraz do wykonania prostych obliczeń.
# 
# 1) Stwórz krotkę `population` zawierającą liczbę ludności w milionach
#    dla pięciu wybranych krajów. Np. Polska - 38, Niemcy - 83 itd.
# 2) Dodaj do krotki `population` dane dla kolejnego kraju używając
#    konkatenacji.
# 3) Wyświetl długość krotki `population`, aby sprawdzić ile jest 
#    obecnie danych.
# 4) Sprawdź, czy liczba 100 (milionów ludności) znajduje się w krotce
#    `population`.
# 5) Wyświetl liczbę ludności dla trzeciego kraju w krotce.
# 6) Oblicz minimalną i maksymalną liczbę ludności w krotce `population`.
# 7) Jeśli maksymalna liczba ludności w krotce jest większa niż 500 mln,
#    wyświetl komunikat: "Znaleziono kraj o bardzo dużej populacji".
#    W przeciwnym razie, wyświetl: "Wszystkie kraje mają populację poniżej 500 mln".
# 

# Polska, Niemcy, Czechy, Rosja, Włochy ----> Populacja w milionach
population = (38, 83, 10, 146, 58) 

# Dodanie Grecji
population += (10, )

print("Obecnych krajów:", (len(population)))

if 100 in population:
    print("Liczba 100 znajduje się w krotce `population`!")
else:
    print("Liczba 100 nie znajduje się w krotce `population`")

# Liczba ludności 3 kraju w krotce --> Czechy
print("Kraj 3 w kolejności:", population[2])

minPopulation = min(population)
maxPopulation = max(population)

print("Minimalna liczba ludności:", minPopulation)
print("Maksymalna liczba ludności:", maxPopulation)

if maxPopulation > 500: 
    print("Znaleziono kraj o bardzo dużej populacji.")
else:
    print("Wszystkie kraje mają populację poniżej 500 mln.")