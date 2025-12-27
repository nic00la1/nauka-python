import random

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None

    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)

class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldsOfStudy = ["IT", "Math", "Robotics"]

    def addStudent(self, student): 
        if isinstance(student1, Student):
            self.studentsList.append(student)
            student.schoolName = self.name
            student.fieldOfStudy = random.choice(self.fieldsOfStudy)

    def printSchoolInfo(self):
        print("School name:", self.name, " City:", self.city)
        print("Students:")
        for s in self.studentsList:
            s.printInfo()

student1 = Student("Nicola", "Kaleta", 19, "Głowno")
student1.schoolName = "Tech School 1"
student1.country = "Poland"
student1.printInfo()
print(student1.country)

student2 = Student("Jola", "Kowalska", 21, "Lublin")

school = School("Tech School", city="Łódź")
school.addStudent(student1)
school.addStudent(student2)
print()
school.printSchoolInfo()
