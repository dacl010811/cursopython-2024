


# Acciones a realizar :  CRUD --> (Create,Read,Update,Delete)
# Acciones de tipo DDL:  Lenguaje de Definicion de Datos : CRear una Tabla o cualquier objeto en la BDD
# Acciones de tipo DML:  Lenguaje de Manipulacion de Datos :  CRUD --> (Create,Read,Update,Delete)

import sqlite3

def crear_conexion(nombre_bdd="bdd_default.db"):
    if nombre_bdd != None:
        conexion = sqlite3.connect(nombre_bdd)
        conexion.close()
    
#crear_conexion("sri.db")

def crear_tabla(nombre_bdd,nombre_tabla="TABLA_1"):
    conexion = sqlite3.connect(nombre_bdd)
    cursor = conexion.cursor()
    sql_ddl = f"CREATE TABLE {nombre_tabla} (nombre VARCHAR(100),edad VARCHAR(10),email VARCHAR(100))"
     
    cursor.execute(sql_ddl) 
    
    conexion.commit()
    conexion.close()  

def insertar_registros(nombre_bdd,nombre_tabla="USUARIOS"):
    conexion = sqlite3.connect(nombre_bdd)
    cursor = conexion.cursor()
    sql_ddl = f"INSERT INTO {nombre_tabla} VALUES ('Darwin Calle1','353','dacl0108112@gmail.com')"
     
    cursor.execute(sql_ddl) 
    
    conexion.commit()
    conexion.close()  

#crear_tabla("sri.db","DARWIN")

insertar_registros("sri.db")

