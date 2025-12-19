# Zadanie do wykonania: 
# 1. Stwórz zmienną decimalNum z wartością dziesiętną 45.6789
# 2. Skonwertuj decimalNum do typu całkowitego (int) i zapisz wynik
#    w zmiennej wholeNum. Wyświetl typ zmiennej wholeNum oraz jej wartość.
# 3. Przekształć łańcuch znaków " 4321 " do typu całkowitego i wyświetl typ po konwersji.
# 4. Stwórz zmienną wholeNum2 z wartością całkowitą 123, nastęnie skonwertuj 
#    ją do typu zmiennoprzecinkowego (float) i wyświetl typ oraz wartość.
# 5. Skonwertuj łańcuch znaków "98.76" do typu zmiennoprzecinkowego i wyświetl
#    typ oraz wartość.
# 6. Skorzystaj z funkcji print do wyświetlenia ciągu tekstu zawierającego
#    wartość wholeNum2, łącząc ją z tekstem oraz innymi typami danych (np.
#    wartością zmiennoprzecinkową, listą). Użyj dwóch metod: konkatenacji
#    za pomocą funkcji str() oraz oddzielenia wartości przecinkami w funkcji print.

decimalNum = 45.6789
wholeNum = int(decimalNum)

print("Typ zmiennej wholeNum:", type(wholeNum), "Wartość:", wholeNum)

lancuch = int(" 4321 ")

print("Typ zmiennej lancuch po konwersji:", type(lancuch))

wholeNum2 = 123
floatNum = float(wholeNum2)
print("Typ zmiennej floatNum:", type(floatNum), "Wartość:", floatNum)


floatNum2 = float("98.76")
print("Typ zmiennej floatNum2", type(floatNum2), "Wartość:", floatNum2)

print(f"Wartość wholeNum2 {str(wholeNum2)}, {str(24.535)} {str([1, 2, 3, 4])}")
print("Wartość wholeNum2", wholeNum2, 235.3422, [2, 35, 6])