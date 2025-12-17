contacts = {
    "Ola" : "ola@example.com",
    "Daniel": 30,
    "Ania": "ania@example.com"
}

contacts["Rafał"] = "rafal@example.com"

print(contacts["Ola"])
print(contacts["Daniel"])
print(type(contacts)) # <class 'dict'>
print(len(contacts))

print(contacts.keys())
print(contacts.values())

for key in contacts:
    print(f"{key}: {str(contacts[key])}")

print("  ")

for key, value in contacts.items(): 
    print(f"{key}: {value}")