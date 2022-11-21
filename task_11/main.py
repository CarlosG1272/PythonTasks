class Vehiculo:
    name = None
    color = None
    windows = None
    motor = None
    year = None
    def __init__(self, name, color, windows, motor, year):
        self.name = name
        self.color = color
        self.windows = windows
        self.motor = motor
        self.year = year
    def getInformation(self):
        print(f"The car {self.name} is color {self.color}, with {self.windows} windows, the motor is {self.motor} and the year of creation is {self.year}")
def createAndSaveInstance():
    tesla = Vehiculo("teslax", "red", 4, "Eléctrico", 2019)
    newFile = open("tesla.bin", "w")
def main():
    pass