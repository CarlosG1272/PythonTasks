import pickle
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
    teslaX = Vehiculo("teslax", "red", 4, "Eléctrico", 2019)
    newFile = open("tesla.bin", "wb")
    pickle.dump(teslaX, newFile)
    newFile.close()

def recoverInstance():
    openFile = open("tesla.bin", "rb")
    teslaRecovery = pickle.load(openFile)
    teslaRecovery.getInformation()

def main():
    createAndSaveInstance()
    recoverInstance()

if __name__ == "__main__":
    main()