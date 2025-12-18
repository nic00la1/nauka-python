# 1. Stwórz zmienną config, która będzie słownikiem
#    z konfiguracją strony internetowej, zapisz w niej
#    poniższe klucze z wartością: 
#    - "website" z wartością "example.com"
#    - "dbType" z wartością "mysql"
#    - "dbUser" z wartością "admin"
#    - "dbPassword" z wartością "12345"
# 2. Pokaż ilość elementów słownika w konsoli
# 3. Pokaż w konsoli wartość klucza "dbType" z słownika
# 4. Wykorzystaj pętle for in aby przejść po wszystkich
#    elementach słownika i pokaż je w konsoli według
#    formatu: 
#    "Klucz w config: website z wartością example.com"

config = {
    "website": "example.com",
    "dbType": "mysql",
    "dbUser": "admin",
    "dbPassword": "12345"
}

print("Ilość elementów słownika w konsoli:", len(config))

print("Wartość klucza dbType z słownika:", config["dbType"])

for key, value in config.items():
    print(f"Klucz w config: {key} z wartością {value}")