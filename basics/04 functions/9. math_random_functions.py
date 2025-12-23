import math
import random

print(type(str(12)))
print(type(str([12, 34])))

number = int("123")
print(type(number))

number += 10
print(number) # 133
print("123" + "10") # 12310

floatNum = float("45.67")
print(type(floatNum))
floatNum *= 2
print(floatNum) # 91.34

print(abs(9)) # wartość bezwzględna
print(abs(-9.1))

print(math.ceil(11.0000001)) # 12 (najmniejsza liczba całkowita, ale nie mniejsza niż podana wartość 11.000001)
print(math.ceil(9.9999999)) # 10
print(math.ceil(-1.000000001)) # -1
print(math.ceil(-1.999999)) # -1

print(math.floor(11.000000001)) # 11
print(math.floor(11.99999999)) # 11
print(math.floor(5.12)) # 5
print(math.floor(-5.12)) # -6
print(math.floor(-5.999999)) # -6

print(max(10, 1, -9, 33, 89, 0)) # 89
print(max([10, 1, -9, 33, 89, 0])) # 89
print(max((10, 1, -9, 33, 89, 0))) # 89
print(min(10, 1, -9, 33, 89, 0)) # -9
print(min([10, 1, -9, 33, 89, 0])) # -9
print(min((10, 1, -9, 33, 89, 0))) # -9

print(4**3) # 64
print(pow(4, 3)) # 64

print(math.sqrt(128)) # 11.31....

print(round(12.7891224, 3)) # 12.789
print(round(12.7891224, 2)) # 12.79
print(round(12.7891224, 1)) # 12.8

print(random.random())
print(random.random() * 100)
print(int(random.random() * 100))

print(random.choice([0, 1, 2, 3, 4]))
print(random.choice(["Ola", "Ania" ,"Adam"]))

print(random.randrange(-10, 30, 5))

listData = [0, 1, 2, 3, 4, 5, 6]
random.shuffle(listData)

print(listData)



