# Stwórz klasę SimCard reprezentującą kartę sim telefonu z kontaktami
# 1) Klasa ustawia atrybut/zmienną klasy contacts jako listę w konstruktorze
# 2) Dodaj metodę addContact przyjmującą oprócz self również parametry
#    name i telephone. Sprawdź z funkcją isinstance czy przekazane dane są
#    prawidłowe, czyli str i int. Stwórz słownik z name i telephone i dodaj go
#    do listy kontaktów obiektu powstałego na bazie klasy.
# 3) Napisz metodę showContacts, która w pętli pokaże kolejne kontakty w terminalu
# 4) Stwórz instancję klasy SimCard
# 5) Dodaj poniższe kontakty: 
#    - "Ola", 987654321
#    - "Adam", 123456789
#    - 100, 123456789
#    - "Kasia", "numer"
#    Część danych jest nieprawidłowa, więc nie powinny być dodane przez addContact
# 6) Wyświetl kontakty z showContacts()

class SimCard:
    def __init__(self):
        self.contacts = []

    def addContacts(self, name, telephone):
        if isinstance(name, str) and isinstance(telephone, int):

            user = {
                "name": name,
                "telephone": telephone
            }

            self.contacts.append(user)
    
    def showContacts(self):
        for c in self.contacts:
            print(c["name"] + " " + str(c["telephone"]))

sim = SimCard()

sim.addContacts("Ola", 987654321)
sim.addContacts("Adam", 123456789)
sim.addContacts(100, 123456789)
sim.addContacts("Kasia", "numer")

sim.showContacts()