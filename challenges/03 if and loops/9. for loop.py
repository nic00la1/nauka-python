# Liczby nieparzyste dodane do set
# 1) Dodaj listę numbers z wartościami od -3 do 3 z krokiem co 1
# 2) Dodaj set z wartością początkową -1 
# 3) Stwórz pętlę for in z tablicą numbers
# 4) W każdej iteracji pętli sprawdź czy liczba z listy jest nieparzysta,
#    czyli reszta z dzielenia przez dwa nie może być równa zero (!= 0).
#    Dodaj nieparzystą liczbę do zestawu.
# 5) Wyświetl w konsoli nieparzyste liczby w set z pomocą pętli for

numbers = [-3, -2, -1, 0, 1, 2, 3]
set = {-1}

for num in numbers:
    if num % 2 != 0:
        set.add(num)

for num in set:
    print(num)