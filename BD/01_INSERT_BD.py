import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

# Insertar en tabla un valor
cursor.execute("INSERT INTO estudiantes VALUES('bluenote@googlemail.com', 'Artes', 'Esperanza',23)")

# Guardamos los cambios haciendo un commit
conexion.commit()

cursor.close()