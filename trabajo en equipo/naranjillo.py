import mysql.connector
from mysql.connector import errorcode

# Configuración de la conexión
config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'PracticaVersionamiento',
    'raise_on_warnings': True
}

def crear_tablas(cursor):
    tablas = {}

    tablas
