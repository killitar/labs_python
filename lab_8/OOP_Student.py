class Student:
    def __init__(self, name = "Ivan", age = 18, groupNumber = "10А"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return print(self.name)

    def getAge(self):
        return print(self.age)

    def getGroupNumber(self):
        return print(self.groupNumber)
    
    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGrupNumber(self, groupNumber):
        self.groupNumber = groupNumber

Alice = Student()
Alice.setNameAge("Alice", 21)
Alice.setGrupNumber("10A")

Natasha = Student()
Natasha.setNameAge("Natasha", 20)
Natasha.setGrupNumber("10B")

Kolya = Student()
Kolya.setNameAge("Kolya", 11)
Kolya.setGrupNumber("11A")

Daniil = Student()
Daniil.setNameAge("Daniil", 128)
Daniil.setGrupNumber("10J")

Pashka = Student()
Pashka.setNameAge("Pashka", 19)
Pashka.setGrupNumber("11B")

Alice.getAge()