

from tkinter import *
from tkinter import messagebox

root = Tk()  # Componente padre
root.title("Hola Mundo Tkinter")
root.config(bg="red")
root.geometry("600x450+50+10")
root.iconbitmap('c:/gui/umbrella_icon_262518.ico')
root.resizable(True, True)
root.config(bg="green")
root.config(relief="sunken")
root.config(border=10)

#Frame
frame = Frame(root,width=600,height=450)
frame.pack(side=LEFT)
frame.pack(anchor=SE)
frame.pack(fill='both',expand=1)
frame.config(bg="yellow")
frame.config(cursor="pirate")
frame.config(relief="sunken")
frame.config(border=25)

#Etiquetas

imagen = PhotoImage(file="c:/gui/linux-gnu.gif",width=60,height=60)
label = Label(frame,text="My primer etiqueta",background="red",foreground="blue",font=("Verdana",24),image=imagen).pack(anchor=NW)
label_1 = Label(frame,text="My segunda etiqueta",background="green",foreground="red").pack(anchor=CENTER)
label_2 = Label(frame,text="My segunda etiqueta",background="green",foreground="red").pack(anchor=SE)

#Text -- Cajas de Texto o Entry

nombre_entry = Entry(frame,foreground="red")
#nombre_entry.grid(row=0,column=1)
nombre_entry.pack()

#Botones
def mostrar_mensaje():
    messagebox.showinfo(message="Prtesionaste el boton")
   
boton_1 = Button(frame,text="Guardar",command=mostrar_mensaje).pack()

#Text Area o text multilinea
#text_area = Text(frame,background="white",foreground="blue",font=("Verdana",24)).pack()

#Radio Button
resultado_selecccion = IntVar()



def selecionar():
    nombre_entry.config(text="Opcion {}".format(resultado_selecccion.get()))



Radiobutton(frame,text="Opcion1",variable=resultado_selecccion,value=10,command=selecionar).pack()
Radiobutton(frame,text="Opcion2",variable=resultado_selecccion,value=20,command=selecionar).pack()
Radiobutton(frame,text="Opcion3",variable=resultado_selecccion,value=30,command=selecionar).pack()

#CheckButon

Checkbutton(frame,text="Azucar",variable=resultado_selecccion,onvalue=1,offvalue=0).pack()
Checkbutton(frame,text="Leche",variable=resultado_selecccion,onvalue=1,offvalue=0).pack()
Checkbutton(frame,text="Chocolate",variable=resultado_selecccion,onvalue=1,offvalue=0).pack()

#Menus en tkinter

menubar_1 = Menu(root)
root.config(menu=menubar_1)

root.mainloop() # Punto de inicio

