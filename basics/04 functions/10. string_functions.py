print("Hello " + "World!")
print("Hello" * 3)

string = "Hello World!"
print(string[0]) # H
print(string[0:5]) # Hello

print("Hello" in string) # True
print("Hello" not in string) # False

multine = """ line 1
line 2 
line 3
"""

print("ala".capitalize())
print("Ola ma kota, Ola ma psa.".count("Ola"))

print("Hello".center(20, "-"))

print(string.startswith("Hello"))
print(string.endswith("World!"))


print(string.find("Ola"))
print(string.find("World"))
print("Ola ma psa, Ola ma kota".rfind("Ola")) # 12

print("4274278".isalnum())
print("4274278.".isalnum())
print("4274278 k".isalnum())

print("4274278 k".isalpha())
print(" kot".isalpha())
print("kot".isalpha())
print("kot2".isalpha())

print("test".islower())
print("teSt".islower())
print("TEST".isupper())

print("TEST".isspace())
print("     \n\n\t".isspace())

print("-|".join(["Ala", "Ola", "Adam"]))

print("Hello World".lower())
print("Hello World".upper())
print("Hello World".swapcase())

print("    \n \t Hello World \n\n  \t".lstrip())
print("    \n \t Hello World \n\n  \t".rstrip())
print("    \n \t Hello          World \n\n  \t".strip())

print("Ola ma psa, Ola ma kota".replace("Ola", "Kasia"))

print("My name is {myName}, I'm from {country}".format(myName = "Nicola", country = "Poland"))
print("My name is {myName}, my postal code is {code}".format(myName = "Nicola", code = 14224))
print("My name is {0}, my postal code is {1}".format("Nicola", 14224))
print("My name is {}, my postal code is {}".format("Nicola", 14224))