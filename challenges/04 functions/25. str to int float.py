# Zadanie na Number:
# 1) Pobierz liczbę całkowitą, od użytkownika do zmiennej 
#    za pomocą funkcji input, przekaż do niej informację: Podaj liczbę całkowitą.
# 2) Zmień typ wartości z tekstu na liczbę całkowitą.
# 3) Stwórz funkcję calculateSquareArea z parametrem height,
#    która zwraca powierzchnię kwadratu.
# 4) Wywołaj funkcję z wcześniej pobraną liczbą całkowitą,
#    wynik pokaż w konsoli.
# 5) Pobierz od użytkownika liczbę dziesiętną, pamiętaj o kropce
#    w liczbie. Oblicz powierzchnię kwadratu z tą wartością,
#    pokaż wynik w konsoli zaokrąglony do 2 miejsc po przecinku.
# 

liczbaCalkowita = int(input("Podaj liczbę całkowitą: "))

def calculateSquareAare(height):
    area = height * height
    area  = round(area, 2)
    print("Powierzchnia kwadratu: ", area, "cm²")
    return area

calculateSquareAare(liczbaCalkowita)

liczbaDziesietna = float(input("Podaj liczbę dziesiętną z kropką: "))

calculateSquareAare(liczbaDziesietna)