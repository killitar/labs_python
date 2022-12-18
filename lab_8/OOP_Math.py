class Math:

    def __init__(self):
        self.a = float(input("a = "))
        self.b = float(input("b = "))
    
    def Addition(self):
        return print(self.a + self.b)

    def Multiplication(self):
        return print(self.a * self.b)

    def Division(self):
        return print(self.a / self.b)

    def Subtraction(self):
        return print(self.a - self.b)


alc = Math()
print("Выберите действие: \n 1 - + \n 2 - * \n 3 - / \n 4 - -")
l = int(input())
if l == 1:
    alc.Addition()
elif l == 2:
    alc.Multiplication()
elif l == 3:
    alc.Division()
elif l == 4:
    alc.Subtraction()
else: 
    print("ащыпка")
