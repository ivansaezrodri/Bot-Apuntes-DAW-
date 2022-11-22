import tratarJS as js
import preguntaBOT as pb
from tkinter import *
import os
import preguntaBOT as pg

def titulo():
    print("""
#############################################################
#                                                           #
#  /$$$$$$$  /$$     /$$   /$$$$$$$$ /$$      /$$  /$$$$$$  #
# | $$__  $$|  $$   /$$/  |__  $$__/| $$  /$ | $$ /$$__  $$ #
# | $$  \ $$ \  $$ /$$/      | $$   | $$ /$$$| $$| $$  \ $$ #
# | $$$$$$$/  \  $$$$//$$$$$$| $$   | $$/$$ $$ $$| $$  | $$ #
# | $$____/    \  $$/|______/| $$   | $$$$_  $$$$| $$  | $$ #
# | $$          | $$         | $$   | $$$/ \  $$$| $$  | $$ #
# | $$          | $$         | $$   | $$/   \  $$|  $$$$$$/ #
# |__/          |__/         |__/   |__/     \__/ \______/  #
#                                                           #
#############################################################\n
    """)

def click():
    respuesta = pg.pregunta(textbox1.get())
    labelTitulo.config(text=respuesta[0])
    labelDuda.config(text=respuesta[1])
    
#titulo()
#print(pb.pregunta(input('Pregunta lo que quieras: ')))

window = Tk()
window.geometry("600x400")
window.title("Bot PY-TWO - Iván Sáez")

## Titulo
labelTitulo = Label(text = "PY-TWO",font=("Noto Sans Display SemiCondensed Black", 48))
labelTitulo.place(x=25,y=25)

## Consulta
labelDuda = Label(text = "¿Alguna duda?")
labelDuda.place(x=25,y=125)

textbox1 = Entry(text= "")
textbox1.place(x=25, y=150, width=550,height=25)
textbox1.focus()

button1 = Button(text= "Buscar",command=click)
button1.place(x=25, y=185, width=550,height=25)

## Descripción

labelTitulo = Label(text = "Concepto",font=("Arial", 28))
labelTitulo.place(x=25, y=250, width=550,height=35)

labelDuda = Label(text = "Definición.")
labelDuda.place(x=30,y=300)


#file:///home/ivarod/Baixades/tkinter.pdf
#file:///home/ivarod/Baixades/tkinter2.pdf


window.mainloop()