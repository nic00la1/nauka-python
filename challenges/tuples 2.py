# 1. Stwórz krotkę z ostatnimi wydatkami na końcie 
#    bankowym z wartościami: 100, 200, 300, 400, 500, 600
# 2. Policz wydatki z pomocą pętli for i wyświetl w konsoli
#    ostateczną kwotę. Pamiętaj, aby stworzyć zmienną
#    z wartością początkową 0 do której dodasz kolejny wydatek

wydatki = (100, 200, 300, 400, 500, 600)
sumaWydatkow = 0
print("Ostatnie wydatki na końcie: ", wydatki)

for el in wydatki: 
    sumaWydatkow += el

print("Suma wydatków: ", sumaWydatkow) 