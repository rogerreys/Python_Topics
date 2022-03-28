import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
 
query = "DROP TABLE IF EXISTS estudiante"
cursor.execute(query)

cursor.close()