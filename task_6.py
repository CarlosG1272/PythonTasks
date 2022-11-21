class Vehiculo:
    Color = None
    Ruedas = None
    Puertas = None
    def __init__(self, color, ruedas, puertas):
        self.Color = color
        self.Ruedas = ruedas
        self.Puertas = puertas

class Coche(Vehiculo):
    Velocidad = None
    Cilindrada = None
    def __init__(self, velocidad, cilindrada, color, ruedas, puertas):
        super().__init__(color, ruedas, puertas)
        self.Velocidad = velocidad
        self.Cilindrada = cilindrada

tesla = Coche(269, 154, "blanco", "aro14", "alas")
print(dir(tesla))
print("El color del coche es", tesla.Color)
print("La velocidad es", tesla.Velocidad)
print("La cilindrada es", tesla.Cilindrada)
print("Las ruedas son", tesla.Ruedas)
print("El tipo de puertas son", tesla.Puertas)
