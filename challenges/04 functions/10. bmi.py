# Zadanie: Kalkulator BMI z funkcją
# 
# Kroki do wykonania: 
# 1) Zdefiniuj funkcję calculateBMI, która przyjmuje wagę w kilogramach i wzrost w centymetrach.
#    Funkcja powinna obliczać BMI i zwracać wartość BMI według wzoru: 
#    weight / ((height / 100) ** 2)
# 2) Zdefiniuj funkcję classifyBMI, która przyjmuje wartość BMI i klasyfikuje ją 
#    do odpowiedniego przedziału.
#    BMI < 18.5 z info: Masz niedowagę.
#    BMI < 25 z info: Twoja waga jest w normie.
#    BMI < 30 z info: Masz nadwagę.
#    reszta wartości to: "Masz sporą nadwagę".
# 3) Poproś użytkownika o wprowadzenie wagi i wzrostu.
# 4) Wywołaj funkcję calculateBMI, aby obliczyć BMI na podstawie danych użytkownika.
# 5) Wywołaj funkcję classifyBMI, aby określić przedział BMI i wyświetlić odpowiedni komunikat.
# 

def calculateBMI(weight, height):
    bmi = weight / ((height / 100) ** 2)
    print("Twoje BMI wynosi:", bmi)
    return bmi

def classifyBMI(bmi):
    if bmi < 18.5:
        print("Masz niedowagę!")
    elif bmi < 25:
        print("Twoja waga jest w normie :)")
    elif bmi < 30:
        print("Masz nadwagę! :O")
    else:
        print("Masz sporą nadwagę!!")

weight = float(input("Wprowadź swoją wagę w kg: "))
height = float(input("Wprowadź swój wzrost w cm: "))

bmi = calculateBMI(weight, height)
classifyBMI(bmi)