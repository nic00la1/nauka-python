# Napisz dwie funkcje konwertujące temperaturę:
# 1) Funkcja cToF skonwertuje stopnie Celsjusza na Fahrenheita, ze wzoru:
#    fahrenheit = celsius * 9 / 5 + 32
# 2) Funkcja fToC konwertuje stopnie Fahrenheita na Celsjusza, ze wzoru:
#    celsius = (fahrenheit - 32) * 5 / 9
# 3) Dodatkowo w konsoli pokaż wynik konwersji, np:
#    "20 stopni Celsjusza to 68 stopni Fahrenheita", itd.
#    Jeśli chcesz użyj w string specjalnego znaku stopni ° za pomocą \xB0
# 4) Skonwertuj 20°C na Fahrenheita (68°F)
#    Skonwertuj 86°F na Celsjusza (30°C)

def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C to {fahrenheit}F°")
    return fahrenheit

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F to {celsius}C°")
    return celsius 

cToF(20)
fToC(86)