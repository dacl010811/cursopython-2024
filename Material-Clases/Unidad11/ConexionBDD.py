

import sqlite3
import time


class Conexion():
    
    __conexion = None
    __cursor = None
    
    def __init__(self,nombre_bdd) -> None:
        try:
            
            self.__conexion = sqlite3.connect(nombre_bdd)
            self.nombre_bdd = nombre_bdd
            
            if self.__conexion != None:
                print("Conexion creada con  èxito!!!")
                time.sleep(2)
        except Exception as e:
            print(f"Error: Al crear la Conexion a la BDD: {nombre_bdd} - {type(e).__name__}")
            

    def cerrar(self):
        try:
            self.__conexion.close()
        except Exception as e:
            print(f"Error al cerrar la conexion de la BDD: {self.nombre_bdd}")
        else:
            print(f"La conexion se cerro con èxito : {self.nombre_bdd}!!")
            time.sleep(1)
            
            
    def crear_tabla(self,nombre_tabla,sql_ddl=None):
        
        try:
            if sql_ddl is None:
                sql_ddl = f"CREATE TABLE {nombre_tabla} (nombre VARCHAR(100),edad VARCHAR(10),email VARCHAR(100),celular VARCHAR(100))"
                                        
            self.__cursor = self.__conexion.cursor()
            self.__cursor.execute(sql_ddl)
            self.__conexion.commit()
            
        except Exception as e:
            print(f"Error al crear la tabla : {nombre_tabla} - Error: {type(e).__name__}")
        else:
            print(f"Tabla  creada con exito : {nombre_tabla}")
            
    def insertar_registros(self,sql_dml):
        
        try:
            self.__cursor = self.__conexion.cursor()
            self.__cursor.execute(sql_dml)
            self.__conexion.commit()
        except Exception as e:
            print(f"Error al insertar registros: {sql_dml} : Error: {type(e).__name__}")
        else:
            print(f"Registros insertados correctamente!!")
                        
    def selecionar_registros(self,nombre_table):
        try:
            sql = f"select * from {nombre_table}"
            
            self.__cursor = self.__conexion.cursor()
            self.__cursor.execute(sql)            
            lista_registros = self.__cursor.fetchall()   # self.__cursor.fetchone()
        except Exception as e:
            print(f"Error al seleccionar registros.  Error: {type(e).__name__}")
            return
        else:
            return lista_registros
        
        
    def selecionar_registro(self,nombre_table):
        try:
            sql = f"select * from {nombre_table}"
            
            self.__cursor = self.__conexion.cursor()
            self.__cursor.execute(sql)            
            fila = self.__cursor.fetchone()   # 
        except Exception as e:
            print(f"Error al seleccionar registro.  Error: {type(e).__name__}")
            return
        else:
            return fila
            
        
        
#Invocacion

conexion_bdd1 = Conexion("conexionBDD.db")

sql_ddl1 = f"CREATE TABLE IF NOT EXISTS NICOLAS_2 (CODIGO VARCHAR(100),nombre VARCHAR(100))"
conexion_bdd1.crear_tabla('',sql_ddl1)

for dato in range(1,5):    
    sql_dml_1 = f'INSERT INTO DARWIN (nombre,edad,email,celular) values ("Nicolas Calle-{dato}",38,"dacl{dato}@gmail.com","0999887244")'
    #conexion_bdd1.insertar_registros(sql_dml_1)
    
datos = conexion_bdd1.selecionar_registros("DARWIN")
dato = conexion_bdd1.selecionar_registro("DARWIN")

for row in  datos:
    print (f"[{row}]")

print(f"La tabla tiene : {len(datos)} ")

print("*******************  fechOne ***********************")
print(f"Dato : {dato}")

conexion_bdd1.cerrar()
