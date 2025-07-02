import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'tu_usuario',       # Cambia aquí tu usuario MySQL
    'password': 'tu_contraseña', # Cambia aquí tu contraseña MySQL
    'host': 'localhost',
}

def crear_base_datos(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS PracticaVersionamiento DEFAULT CHARACTER SET 'utf8'")
        print("Base de datos creada o ya existe.")
    excep
