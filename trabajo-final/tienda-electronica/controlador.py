import time
import sqlite3

class ConexionBDD():

    __conexion = None
    __cursor = None

    def __init__(self, nombre_bdd) -> None:
        try:
            self.nombre_bdd = nombre_bdd
            self.__conexion = sqlite3.connect(nombre_bdd)
            if self.__conexion != None:
                print(f"Conexion creada con éxito")
                time.sleep(2)
        except Exception as e:
            print(
                f"Error al crear la conxion a la BDD: {nombre_bdd} - Error: {type(e).__name__}")
        else:
            self.__cursor = self.__conexion.cursor()

    def cerrar(self):
        try:
            self.__conexion.close()
        except Exception as e:
            print(
                f"Error al cerrar conexión a la BDD: {self.nombre_bdd} -  Error: {type(e).__name__}")
        else:
            print(
                f"La conexiona a la BDD: {self.nombre_bdd}, se cerro con éxito!!")
            time.sleep(0.25)

    def crear_tabla(self, sql_ddl):
        try:
            self.__cursor.execute(sql_ddl)
            self.__conexion.commit()
        except Exception as e:
            print(
                f"Error al crear tabla en la BDD: {self.nombre_bdd} -  Error: {type(e).__name__}")
        else:
            print(f"Se creo la tabla exitosamente en : {self.nombre_bdd}")
            time.sleep(0.25)

    def select_all(self, nombre_tabla):
        try:
            sql = f"select * from {nombre_tabla}"
            self.__cursor.execute(sql)
            filas = self.__cursor.fetchall()
        except Exception as e:
            print(
                f"Error al seleccionar filas en : {nombre_tabla} : Error: {type(e).__name__}  ")
            return None
        else:
            return filas

    def insertar_registro(self, sql_dml) -> bool:
        isInsert = False
        try:
            if sql_dml != None:
                self.__cursor.execute(sql_dml)
                time.sleep(0.25)
                self.__conexion.commit()
        except Exception as e:
            print(
                f"Error al insertar filas en : {sql_dml} : Error: {type(e).__name__}  ")
        else:            
            print(f"Insersión realizada, con éxito!!")
            isInsert = True
        
        return isInsert
    
    def truncate_tabla(self, nombre_tabla):
        try:
            sql_dml = f"delete from {nombre_tabla}"
            if sql_dml != None:
                self.__cursor.execute(sql_dml)
                time.sleep(1)
                self.__conexion.commit()
        except Exception as e:
            print(
                f"Error al truncar tabla : {nombre_tabla} : Error: {type(e).__name__}  ")
        else:
            print(f"El truncate se realizó con éxito!!")



