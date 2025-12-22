# Zadanie: Obliczanie pola powierzchni prostokąta
#
# Cel: Napisz program, który oblicza pole powierzchni prostokąta. Program
# powinien prosić użytkownika o wprowadzenie długości i szerokości prostokąta,
# a następnie obliczyć jego pole powierzchni.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję calculateArea, która przyjmuje dwa parametry: length i width.
#    Funkcja ta powinna obliczać pole powierzchni prostokąta i zwracać wynik.
# 2) Poproś użytkownika o wprowadzenie długości prostokąta.
# 3) Poproś użytkownika o wprowadzenie szerokości prostokąta.
# 4) Wywołaj funkcję calculateArea z wprowadzonymi wartościami i przechowaj wynik.
# 5) Wyświetl wynik obliczeń użytkownikowi
#

def calculateArea(length, width):

    length = int(input("Wprowadź długość prostokąta: "))
    width = int(input("Wprowadź szerokość prostokąta: "))

    area = length * width
    print(f"Pole prostokąta o wymiarach {length} x {width} = {area}cm")
    return area

calculateArea(any, any)