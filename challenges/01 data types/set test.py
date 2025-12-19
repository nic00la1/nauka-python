# 1. Stwórz set z unikalnymi wartościami jak: 
#    Ania, Kasia, Ola, Karol, Daniel, Zuza
# 2. Dodaj do set za pomocą funkcji add kolejne elementy: 
#    Olek, Basia, Kasia, Karol, Zuza, Paulina
# 3. Pokaż w konsoli wielkość set
# 4. Wykorzystaj pętlę for aby pokazać elementy w set

setNames = {"Ania", "Kasia", "Ola", "Karol", "Daniel", "Zuza"}

setNames.add("Olek")
setNames.add("Basia")
setNames.add("Kasia")
setNames.add("Karol")
setNames.add("Zuza")
setNames.add("Paulina")

print("Wielkość setNames:", len(setNames))

for el in setNames:
    print(el)