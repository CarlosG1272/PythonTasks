import sqlite3
def initConnection():
    conn = sqlite3.connect("testDB")
    cursor = conn.cursor()
    return conn, cursor

def insertAlumnos():
    conn, cursor = initConnection()
    names = ("Jorge", "Carlos", "Luis", "Julian", "Leonel", "Sergio", "Pedro", "Goku")
    apellidos = ("Menendez", "Guerra", "Sanchez", "De la paz", "Calvo", "De la cruz", "Diaz","Quispe")
    counter = 1
    for name in names:
        query = f'INSERT INTO Alumnos(id, nombre, apellido) VALUES({counter}, "{name}", "{apellidos[counter-1]}")'
        cursor.execute(query)
        counter += 1
    conn.commit()
    cursor.close()
    conn.close()

def readAndPrintData(name):
    conn, cursor = initConnection()
    query = f'SELECT * FROM Alumnos WHERE nombre="{name}"'
    coincidenceData = cursor.execute(query)
    finalData = coincidenceData.fetchone()
    cursor.close()
    conn.close()
    return finalData
def main():
    # Insert students in the first instance
    insertAlumnos()
    # Case 1, select the student with name Carlos
    print(readAndPrintData("Carlos"))
    # Case 2, select the student with name Goku
    print(readAndPrintData("Goku"))

if __name__ == "__main__":
    main()