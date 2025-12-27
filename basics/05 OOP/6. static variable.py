class Employee:
    numEmployees = 0
    employeesList = []

    def __init__(self, name):
        self.name = name

        Employee.numEmployees += 1
        print(self.name, "numEmployees: ", Employee.numEmployees)

        Employee.employeesList.append(self)

    def printAllEmployees(self):
        for el in Employee.employeesList:
            print(el.name)

employee1 = Employee("Ola")
employee1 = Employee("Kasia")
employee1 = Employee("Adam")
employee1 = Employee("Karol")
employee1 = Employee("Kamil")
employee1 = Employee("Karolina")
employee1 = Employee("Amelia")
employee1 = Employee("Oliwia")

print("Employee.numEmployees:", Employee.numEmployees)
print()

employee1.printAllEmployees()
