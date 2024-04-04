from tkinter import *
import tkinter as tk
from tkinter import messagebox
from controlador import ConexionBDD
from modelo import Cliente

# Representar la GUI para el usuario

class Tienda(Tk):
    
    __frame = None
    __root = None
    
    def __init__(self,screenName=None,baseName=None,className="Tk",useTk=True,sync=False,use=None,titulo="Ventana",tamanio="600x300") -> None:        
        Tk.__init__(self,screenName, baseName, className, useTk, sync, use)
        
        self.titulo = titulo
        self.tamanio = tamanio
        
        self.__frame = Frame()
        
        #Crear menu
        self.menubar = Menu(self)  
        self.config(menu=self.menubar)
        
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Nuevo")
        self.filemenu.add_command(label="Abrir")
        self.filemenu.add_command(label="Guardar")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Salir",command=self.quit)
        
        self.menubar.add_cascade(label="Archivo",menu=self.filemenu)
        
        self.configurar_ventana(self.titulo,self.tamanio)
        self.centar_ventana()
        
        #Mostrar Componetes dentro del Frame
        self.mostrar_componentes()
        self.__frame.pack()
        
    
    
    def configurar_ventana(self,titulo,tamanio):
        self.title(titulo)
        self.geometry(tamanio)
        
    def centar_ventana(self):
        try:
            self.update_idletasks()
            width = self.winfo_width() # Capturando el valor de X de la ventana
            height = self.winfo_height() # Capturando el valor de y de la ventana
            
            x = ((self.winfo_screenwidth() // 2) - (width // 2)) 
            y = ((self.winfo_screenheight() // 2) - (height // 2))
            
            self.geometry("{}x{}+{}+{}".format(width,height,x,y))
            
        except Exception as e:
            print(f"Error al redimensionar ventana - Error: {type(e).__name__}")
    
    
    def obterner_datos_cliente_gui(self)-> Cliente:
        
        cliente_nuevo = None
        
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        cedula = self.cedula_entry.get()
        email = self.email_entry.get()
        
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()
        sector = self.sector_entry.get()
        celular = self.celular_entry.get()
        
        if nombre and apellido and cedula and email and telefono and direccion and sector and celular:
            cliente_nuevo = Cliente(nombre,apellido,cedula,email,telefono,direccion,sector,celular)
            
            print(f"Cliente : {cliente_nuevo}")
        else:
            messagebox.showwarning("Registrar Cliente","Por favor llenar todos los campos requeridos")
        
        
        return cliente_nuevo;
    
    def regristrar_cliente(self):
        try:
            print("Registrar cliente")
            cliente = self.obterner_datos_cliente_gui()
            
            if cliente and isinstance(cliente,Cliente):
                self.cliente_lista.insert(tk.END,cliente)            
        except Exception as e:
            print(f"Error al registrar Cliente Lista. Error: {type(e).__name__}")
            
    
    def regristrar_cliente_bdd(self):
        try:
            print("Registrar cliente BDD")
            cliente = self.obterner_datos_cliente_gui()  
                      
            if cliente and isinstance(cliente,Cliente):
                
                sql_ddl = """CREATE TABLE IF NOT EXISTS CLIENTE
                        ( NOMBRE VARCHAR(100),
                          APELLIDO VARCHAR(100),
                          CEDULA VARCHAR(100),
                          EMAIL VARCHAR(100),
                          TELEFONO VARCHAR(100),
                          DIRECCION VARCHAR(100),
                          SECTOR VARCHAR(100),
                          CELULAR VARCHAR(100)
                        )"""
                
                sql_dml = "INSERT INTO CLIENTE (NOMBRE,APELLIDO,CEDULA,EMAIL,TELEFONO,DIRECCION,SECTOR,CELULAR) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    cliente.nombre,
                    cliente.apellido,
                    cliente.cedula,
                    cliente.email,
                    cliente.telefono,
                    cliente.dirección,
                    cliente.sector,
                    cliente.celular
                )
                
                print(f"SQL : {sql_dml}")
                
                conexion_bdd = ConexionBDD("tienda.db")
                conexion_bdd.crear_tabla(sql_ddl)
                
                if conexion_bdd.insertar_registro(sql_dml):
                    messagebox.showinfo("Registar CLiente BDD","Cliente Registrado con exito en la BDD.")    
            else:
                messagebox.showerror("Registar CLiente BDD","Error al registart cliente a la BDD")
                                                           
        except Exception as e:
            print(f"Error al registrar Cliente BDD. Error: {type(e).__name__}")
    
    
    
    def mostrar_componentes(self):
        
        self.nombre_label = tk.Label(self.__frame, text="Nombre")
        self.nombre_label.grid(row=0,column=0,padx=5,pady=5)
        self.nombre_entry = tk.Entry(self.__frame)
        self.nombre_entry.grid(row=0,column=1,padx=5,pady=5)
        
        self.apellido_label = tk.Label(self.__frame, text="Apellido")
        self.apellido_label.grid(row=1,column=0,padx=5,pady=5)
        self.apellido_entry = tk.Entry(self.__frame)
        self.apellido_entry.grid(row=1,column=1,padx=5,pady=5)
        
        self.cedula_label = tk.Label(self.__frame, text="Cedula")
        self.cedula_label.grid(row=2,column=0,padx=5,pady=5)
        self.cedula_entry = tk.Entry(self.__frame)
        self.cedula_entry.grid(row=2,column=1,padx=5,pady=5)
        
        self.email_label = tk.Label(self.__frame, text="Email")
        self.email_label.grid(row=3,column=0,padx=5,pady=5)
        self.email_entry = tk.Entry(self.__frame)
        self.email_entry.grid(row=3,column=1,padx=5,pady=5)
        
        # Columa 2 de COmponentes
        self.telefono_label = tk.Label(self.__frame, text="Telefono")
        self.telefono_label.grid(row=0,column=2,padx=5,pady=5)
        self.telefono_entry = tk.Entry(self.__frame)
        self.telefono_entry.grid(row=0,column=3,padx=5,pady=5)
        
        self.direccion_label = tk.Label(self.__frame, text="Direccion")
        self.direccion_label.grid(row=1,column=2,padx=5,pady=5)
        self.direccion_entry = tk.Entry(self.__frame)
        self.direccion_entry.grid(row=1,column=3,padx=5,pady=5)
        
        self.sector_label = tk.Label(self.__frame, text="Sector")
        self.sector_label.grid(row=2,column=2,padx=5,pady=5)
        self.sector_entry = tk.Entry(self.__frame)
        self.sector_entry.grid(row=2,column=3,padx=5,pady=5)
        
        self.celular_label = tk.Label(self.__frame, text="Celular")
        self.celular_label.grid(row=3,column=2,padx=5,pady=5)
        self.celular_entry = tk.Entry(self.__frame)
        self.celular_entry.grid(row=3,column=3,padx=5,pady=5)
        
        #Botones
        
        self.registar_btn = tk.Button(self.__frame, text="Agregar Cliente",command=self.regristrar_cliente)
        self.registar_btn.grid(row=5,column=1,padx=5,pady=5)
        
        self.guardar_btn = tk.Button(self.__frame, text="Guardar Cliente BDD",command=self.regristrar_cliente_bdd)
        self.guardar_btn.grid(row=5,column=2,padx=5,pady=5)
        
        #ListBox
        
        self.cliente_lista = tk.Listbox(self.__frame, width=100 )
        self.cliente_lista.grid(row=6,column=0,pady=5,columnspan=4)
        
                                        
        
#Invocacion

app = Tienda(titulo="Tienda Electronica",tamanio="650x400")
app.mainloop()


        
        
        
        
        

