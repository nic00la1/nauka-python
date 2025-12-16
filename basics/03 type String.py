str = "Hello World!"
print(str)
print(len(str))
print(type(str))

print(str[len(str) - 1])


print(str[0:5]) # Hello

print(str * 4)

strX3 = str * 3
print(strX3)

str2 = str + " and Hello again!"
print (str2)

print(str2[6:]) # World! and Hello again!

print(str2[::3]) # Hlwl deogn

multiline = """
Pierwsza linia
Druga linia
Trzecia linia
"""

print(multiline)

multiline2 = "Pierwsza linia\nDruga linia\nTrzecia \t linia \" \\"
print(multiline2)