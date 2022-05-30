import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM estudiantes")
estudiantes = cursor.fetchall()

for i in estudiantes:
    print(f"Correo:{i[0]}", f"\tEdad:{i[3]}")

cursor.close()
