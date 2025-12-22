# Cel: Napisz program, który analizuje wprowadzone temperatury i wykrywa ich średnią, 
# najniższą oraz najwyższą wartość. Program powininen prosić użytkownika o wprowadzenie
# temperatur jedna po drugiej, a następnie zwracać raport analizy.
# Komentarze w kodzie będą po polsku, a nazwy zmiennych i funkcji po angielsku.
#
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie serii temperatur, gdzie każda temperatura wprowadzana jest
#    oddzielnie, a zakończenie wprowadzania sygnalizowane jest przez wpisanie 'koniec'.
# 2) Dla każdej wprowadzonej temperatury, dodaj ją do listy temperatur po konwersji na typ float.
# 3) Po zakończeniu wprowadzania danych, wywołaj funkcję analizującą temperatury, która zwraca
#    krotkę zawierającą średnią, maksymalną i minimalną temperaturę z listy.
#    Uwaga, aby pobrać wartość minimalną z listy wykorzystaj funkcję min(), do której przekażesz
#    listę wartości liczbowych, tak samo max() oraz sum()
# 4) Wyświetl wyniki analizy użytkownikowi.
#
# Rozwiązanie:

temperatures = []

while True:
    temp = input("Wprowadź kolejną temperaturę lub 'koniec', aby zakończyć: ")

    if temp.lower() == "koniec":
        break
    else:
        temperatures.append(float(temp))

print("\nLista temperatur nieuporządkowana: ")
print(temperatures)

def analyzeTemperatures(temperatures):
    print("\nWyniki Analizy: ")
    average = sum(temperatures) / len(temperatures)
    minTemp = min(temperatures)
    maxTemp = max(temperatures)

    tupleTemperatures = (round(average, 2), minTemp, maxTemp)
    print(tupleTemperatures)
    return tupleTemperatures

analyzeTemperatures(temperatures)