

# Acciones a realizar :  CRUD --> (Create,Read,Update,Delete)
# Acciones de tipo DDL:  Lenguaje de Definicion de Datos : CRear una Tabla o cualquier objeto en la BDD
# Acciones de tipo DML:  Lenguaje de Manipulacion de Datos :  CRUD --> (Create,Read,Update,Delete)

import sqlite3


def crear_conexion(nombre_bdd="bdd_default.db"):
    if nombre_bdd != None:
        conexion = sqlite3.connect(nombre_bdd)
        conexion.close()




def crear_tabla(nombre_bdd, nombre_tabla="TABLA_1"):
    conexion = sqlite3.connect(nombre_bdd)
    cursor = conexion.cursor()
    sql_ddl = f"CREATE TABLE {nombre_tabla} (nombre VARCHAR(100),edad VARCHAR(10),email VARCHAR(100))"

    cursor.execute(sql_ddl)

    conexion.commit()
    conexion.close()


def insertar_registros(nombre_bdd, nombre_tabla="USUARIOS"):
    conexion = sqlite3.connect(nombre_bdd)
    cursor = conexion.cursor()
    for row in range(1,101):
        sql_ddl = f"INSERT INTO {nombre_tabla} VALUES ('Darwin Calle-{row}','3532','dacl01081122@gmail.com')"
        print(f"row: {row}")
        cursor.execute(sql_ddl)
        conexion.commit()
    else:
        print("Los registros se insertaron con exito!!")
    
    conexion.close()


def  insertar_multiples_filas(nombre_bdd, nombre_tabla="USUARIOS"):
    
    lista_usuarios = [("Juan Bautista 1",40,"dacloi1@gmail.com"),
                ("Juan Bautista 2",40,"dacloi2@gmail.com"),
                ("Juan Bautista 3",40,"dacloi3@gmail.com"),
                ("Juan Bautista 4",40,"dacloi4@gmail.com"),
                ("Juan Bautista 5",40,"dacloi5@gmail.com"),
                ("Juan Bautista 6",40,"dacloi6@gmail.com"),
                ("Juan Bautista 7",40,"dacloi6@gmail.com")
                ]
    
    conexion = sqlite3.connect(nombre_bdd)
    cursor = conexion.cursor()
    #sql_ddl = f"INSERT INTO {nombre_tabla} VALUES ('?','?','?')"
    
    cursor.executemany("INSERT INTO USUARIOS VALUES (?,?,?)",lista_usuarios) # Multiple insersiòn
    conexion.commit()
    conexion.close()
    

def  seleccionar_info(nombre_bdd, nombre_tabla="USUARIOS"):
    conexion = sqlite3.connect(nombre_bdd)
    cursor = conexion.cursor()
    
    # ME trae todos los registros de la tabla . (*)
    cursor.execute(f"select * from {nombre_tabla} ")
    print(cursor)
    
    #Metodo fechone(): El primer registro de la tabla (1)
    usuario_select = cursor.fetchone()  # Lectura simple
    print(usuario_select)
    
    #
    usuario_select_1 = cursor.fetchall() # Lectura multiple
    for usuario in usuario_select_1:
        print(usuario)
    
    conexion.close()
    
    
    


# Invocacion

#crear_conexion("sriFinal.db")
#crear_tabla("sriFinal.db","USUARIOS")

#insertar_registros("sriFinal.db")

#insertar_multiples_filas("sriFinal.db")

seleccionar_info("sriFinal.db")