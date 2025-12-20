num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbę startową:"))
        reset = False

    operation = input("Podaj operację artymetyczną jak, np." 
                      + str(calcOperations) + " lub exit jeśli koniec lub reset: ")
    if operation == "exit": break
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOperations:
        print("Nieprawidłowa operacja, spróbuj ponownie.")
        continue

    secondNum = int(input("Podaj drugą liczbę: "))

    if operation == "+":
        result = num + secondNum
    
    if operation == "-":
        result = num - secondNum

    if operation == "*":
        result = num * secondNum
    
    if operation == "/":
        result = num / secondNum

    if operation == "**":
        result = num ** secondNum

    print(f"Wynik: {num} {operation} {secondNum} = {result}")
    num = result
    result = None
