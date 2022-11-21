class Alumno:
    nombre = None
    nota = None
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def verInformacion(self):
        print("El nombre del alumno es", self.nombre)
        print("La nota obtenida de", self.nombre, "es", self.nota)
    def aprobo(self):
        if self.nota < 5:
            print("El alumno", self.nombre,"no aprobó")
        else:
            print("El alumno", self.nombre, "si aprobó")

print("Alumno 1:")
alumno1 = Alumno("Carlos", 9.5)
alumno1.verInformacion()
alumno1.aprobo()
print("")
print("Alumno 2:")
alumno2 = Alumno("Max", 4)
alumno2.verInformacion()
alumno2.aprobo()