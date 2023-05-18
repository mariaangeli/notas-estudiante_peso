#------------------------------------------
#-------Notas-Estudiante_Peso--------------
#------------------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox



#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Notas y peso")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="purple")


#abrir toplevel notas
def abrir_toplevel_Notas():
    global toplevel_Notas
    toplevel_Notas = Toplevel()
    toplevel_Notas.title("Notas")
    toplevel_Notas.resizable(False, False)
    toplevel_Notas.geometry("300x200")
    toplevel_Notas.config(bg="Violeta")

    #--------------------------------
    # frame entrada datos
    #--------------------------------

    # etiqueta para valor de Materias
    lb_c = Label(frame_entrada, text = "Materias = ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=200, y=60)
    





#abrir toplevel peso_estatura
def abrir_toplevel_peso_estatura():
    global toplevel_peso_estatura
    toplevel_peso_estatura = Toplevel()
    toplevel_peso_estatura.title("peso_estatura")
    toplevel_peso_estatura.resizable(False, False)
    toplevel_peso_estatura.geometry("300x200")
    toplevel_peso_estatura.config(bg="white")

    # logo de la app
    lb_logo2 = Label(toplevel_Notas, image=logo, bg="white")
    lb_logo2.place(x=10,y=10)

    # etiqueta para valor en Notas
    lb_c = Label(toplevel_Notas, text = "N = ")
    lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_c.place(x=150, y=60)





#--------------------------------
# variables globales
#--------------------------------
Nombre = StringVar()
Apellidos = StringVar()
Correo = StringVar()
notas = StringVar()
peso_estatura = StringVar()
tk = StringVar()
kf = StringVar(value="notas peso")

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=500, height=500)
frame_entrada.place(x=0, y=10)

# logo de la app
logo = PhotoImage(file="img/Logo.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=44,y=10)

# titulo de la app
titulo = Label(frame_entrada, text="Notas_Peso")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

# boton para peso y estatura
peso_estatura=PhotoImage(file="img/Peso y Estatura.png")
bt_peso_estatura = Button(frame_entrada, command=abrir_toplevel_peso_estatura)
bt_peso_estatura.config(image=peso_estatura, width=200, height=200)
bt_peso_estatura.place(x=60, y=200)

#boton para las Notas
Notas = PhotoImage(file="img/Notas.png")
bt_Notas =Button(frame_entrada, command=abrir_toplevel_Notas)
bt_Notas.config(image=Notas, width=200, height=200)
bt_Notas.place(x=250, y=200)

#----------------------------------
#------frame resultados------------
#----------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=500, height=100)
frame_resultados.place(x=10, y=399)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=460,height=160)

# etiqueta para valor de nombre
lb_c = Label(frame_entrada, text = "Nombre = ")
lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_c.place(x=200, y=60)

# caja de texto para valor de nombre
entry_nombre = Entry(frame_entrada, textvariable=Nombre)
entry_nombre.config(bg="white", fg="blue", font=("Times New Roman", 18), width=12)
entry_nombre.focus_set()
entry_nombre.place(x=310,y=60)

# etiqueta para valor de apellido
lb_c = Label(frame_entrada, text = "Apellidos = ")
lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_c.place(x=200, y=100)

# caja de texto para el valor de  Apellidos
entry_Apellidos = Entry(frame_entrada, textvariable=Apellidos)
entry_Apellidos.config(bg="white", fg="blue", font=("Times New Roman", 18), width=12)
entry_Apellidos.focus_set()
entry_Apellidos.place(x=315,y=100)

# etiqueta para valor de Correo
lb_c = Label(frame_entrada, text = "Correo = ")
lb_c.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_c.place(x=200, y=150)

# caja de texto para el valor de  Correo
entry_Correo = Entry(frame_entrada, textvariable=Correo)
entry_Correo.config(bg="white", fg="blue", font=("Times New Roman", 18), width=12)
entry_Correo.focus_set()
entry_Correo.place(x=315,y=150)

#run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()

