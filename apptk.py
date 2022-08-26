from tkinter import *
ventana = Tk()
ventana.title("Calculadora.PY")
ventana.resizable(False, False)
ventana.iconbitmap("C:\\Users\\Nicolas Cax\\Downloads\\evilfaceicon.ico")
e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row= 0, column= 0, columnspan= 4, padx= 5, pady= 5)
ventana.config(background = "#1f2f75")

i = 0

def clickBoton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def operation():
    ecuation = e_texto.get()
    resultado = eval(ecuation)
    e_texto.delete(0, END)
    e_texto.insert(0,resultado)
    i = 0

boton1 = Button(ventana, text= "1", width= 5, height= 2, command = lambda :clickBoton(1))
boton2 = Button(ventana, text= "2", width= 5, height= 2, command = lambda :clickBoton(2))
boton3 = Button(ventana, text= "3", width= 5, height= 2, command = lambda :clickBoton(3))
boton4 = Button(ventana, text= "4", width= 5, height= 2, command = lambda :clickBoton(4))
boton5 = Button(ventana, text= "5", width= 5, height= 2, command = lambda :clickBoton(5))
boton6 = Button(ventana, text= "6", width= 5, height= 2, command = lambda :clickBoton(6))
boton7 = Button(ventana, text= "7", width= 5, height= 2, command = lambda :clickBoton(7))
boton8 = Button(ventana, text= "8", width= 5, height= 2, command = lambda :clickBoton(8))
boton9 = Button(ventana, text= "9", width= 5, height= 2, command = lambda :clickBoton(9))
boton0 = Button(ventana, text= "0", width= 15, height= 2, command = lambda :clickBoton(0))

Bdelete= Button(ventana, text= "AC", width= 5, height= 2, command = lambda :borrar())
BParentecis1 = Button(ventana, text= "(", width= 5, height= 2, command = lambda :clickBoton("("))
BParentecis2 = Button(ventana, text= ")", width= 5, height= 2, command = lambda :clickBoton(")"))
BIgual = Button(ventana, text= "=", width= 5, height= 2, command = lambda :operation())
BPunto = Button(ventana, text= ".", width= 5, height= 2, command = lambda :clickBoton("."))

Bsuma = Button(ventana, text= "+", width= 5, height= 2, command = lambda :clickBoton("+"))
BResta = Button(ventana, text= "-", width= 5, height= 2, command = lambda :clickBoton("-"))
BMultiplicacion = Button(ventana, text= "x", width= 5, height= 2, command = lambda :clickBoton("*"))
BDivision = Button(ventana, text= "/", width= 5, height= 2, command = lambda :clickBoton("/"))

Bdelete.grid(row= 1, column= 0, padx= 5, pady= 5)
BParentecis1.grid(row= 1, column= 1, padx= 5, pady= 5)
BParentecis2.grid(row= 1, column= 2, padx= 5, pady= 5)
BDivision.grid(row= 1, column= 3, padx= 5, pady= 5)

boton7.grid(row= 2, column= 0, padx= 5, pady= 5)
boton8.grid(row= 2, column= 1, padx= 5, pady= 5)
boton9.grid(row= 2, column= 2, padx= 5, pady= 5)
BMultiplicacion.grid(row= 2, column= 3, padx= 5, pady= 5)

boton4.grid(row= 3, column= 0, padx= 5, pady= 5)
boton5.grid(row= 3, column= 1, padx= 5, pady= 5)
boton6.grid(row= 3, column= 2, padx= 5, pady= 5)
Bsuma.grid(row= 3, column= 3, padx= 5, pady= 5)

boton1.grid(row= 4, column= 0, padx= 5, pady= 5)
boton2.grid(row= 4, column= 1, padx= 5, pady= 5)
boton3.grid(row= 4, column= 2, padx= 5, pady= 5)
BResta.grid(row= 4, column= 3, padx= 5, pady= 5)

boton0.grid(row= 5, column= 0,columnspan= 2, padx= 5, pady= 5)
BPunto.grid(row= 5, column= 2, padx= 5, pady= 5)
BIgual.grid(row= 5, column= 3, padx= 5, pady= 5)

ventana.mainloop()
