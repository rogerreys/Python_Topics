import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

# INSERT IN TABLE SEVERAL VALUES
usuarios = [
    ('parrillaexquisita@vip.com','Arquitectura','Giulia', 26),
    ('lollipopbusiness@vip.com','Contaduría','Rosana', 60),
    ('solfernandez@googlemail.com','Estadística','Sol', 30),
    ('carlitos@googlemail.com','Computación','Carlos', 60),
    ('imprentadetata@vip.com','Periodismo','Luciano', 21)
]

cursor.executemany("INSERT INTO estudiantes VALUES(?,?,?,?)", usuarios)

conexion.commit()
cursor.close()