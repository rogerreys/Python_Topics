import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

query = "SELECT * FROM estudiantes"
cursor.execute(query)

estudiante = cursor.fetchone()
print(estudiante)

cursor.close()