class Car:

    def __init__(self, color = 'Черный', type = 'Седан', year = 2008):
        self.color =  color
        self.type = type
        self.year = year

    def start(self):
        return("Автомобиль заведен")

    def stop(self):
        return("Автомобиль заглушен")

    def setYear(self, year):
        self.year = year

    def setType(self, type):
        self.type = type

    def setColor(self, color):
        self.color = color