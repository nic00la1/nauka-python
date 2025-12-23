# Zadanie z lambdą i map
# 1) Stwórz listę names z wartościami Ola, Ania, Kasia
# 2) Z pomocą mapy i lambdy, dodaj do każdego imienia tekst " Kowalska"
# 3) Wyświetl nową listę w konsoli
# 4) Przefiltruj nową listę ze względu na długość tekstu, zachowaj
#    w nowej liście tylko te, które mają więcej niż 12 znaków
#    Pokaż przefiltrowaną listę w konsoli.

names = ("Ola", "Ania", "Kasia")

result = list(map(lambda name: name + " Kowalska", names))
print(result)

result2 = list(filter(lambda name: len(name) > 12, result))
print(result2)