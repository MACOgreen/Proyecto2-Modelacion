from os import system
import sys
from tkinter import *
from VentanaCpm import cpm
data = [
    {
        "activity": "start",
        "duration": 0,
        "predecessors": [],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "a",
        "duration": 2,
        "predecessors": ["start"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "b",
        "duration": 5,
        "predecessors": ["start"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "c",
        "duration": 4,
        "predecessors": ["a"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "d",
        "duration": 6,
        "predecessors": ["b", "c"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "e",
        "duration": 3,
        "predecessors": ["d"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "f",
        "duration": 8,
        "predecessors": ["e"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "g",
        "duration": 10,
        "predecessors": ["e"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
    {
        "activity": "end",
        "duration": 0,
        "predecessors": ["f", "g"],
        "es": 0,
        "ef": 0,
        "ls": 0,
        "lf": 0,
    },
]

ventana = Tk()

##Configuracion la ventana
ventana.geometry("500x300+500+190")
ventana.title("Sistema de almacenamiento de actividades.")
ventana.resizable(width=False,height=False)
##

##Titulo de la ventana
titulo= Label(ventana,text="Bienvenido! Para comenzar ,cargue un archivo.",font=("Arial",12))
titulo.place(x=95,y= 20)
##

### Funciones
def salir():
    sys.exit()

def vcpm():
    cpm(data)

###


### Botones 

##Boton de carga de archivo
boton_cargar=Button(ventana,text="Cargar archivo",font=("Arial",11))
boton_cargar.place(x=190,y=80)
boton_cargar.config(width=15,height=2)
##

##Boton para mostrar el grafo
boton_grafo=Button(ventana,text="Mostrar Grafo",font=("Arial",11))
boton_grafo.place(x=190,y=130)
boton_grafo.config(width=15,height=2)
##

##Boton para aplicar CPM
boton_cpm=Button(ventana,text="Aplicar Pert Cpm",font=("Arial",11),command=vcpm)
boton_cpm.place(x=190,y=180)
boton_cpm.config(width=15,height=2)
##

##Boton para salir del sistema
boton_out=Button(ventana,text="Salir del sistema",font=("Arial",11),command=salir)
boton_out.place(x=190,y=230)
boton_out.config(width=15,height=2)
##

###



ventana.mainloop()
