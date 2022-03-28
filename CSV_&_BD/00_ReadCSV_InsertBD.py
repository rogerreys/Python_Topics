import sqlite3
import csv

conexion = sqlite3.connect(r"/home/roger/Escritorio/PROGRAMAS/DEV_SOFT/PYTHON/DATOS_VIS/BD/ejemplo.db")
cursor = conexion.cursor()

path_file = "/home/roger/Escritorio/PROGRAMAS/DEV_SOFT/PYTHON/DATOS_VIS/CSV_&_BD/datos_db.txt"
# Decodificar
file = open(path_file, encoding='latin-1')
rows = csv.reader(file)


cursor.executemany("INSERT INTO estudiantes VALUES(?,?,?,?)",rows)
cursor.execute("SELECT * FROM estudiantes")
print(cursor.fetchall())

conexion.commit()
cursor.close()
