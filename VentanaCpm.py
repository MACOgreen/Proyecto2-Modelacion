from tkinter import *
from cpm import cpm_algorithm, get_critical_path,create_graph, order_data

def cpm(data):

    ventana = Tk()
    ##Configuracion la ventana
    ventana.geometry("500x300+500+190")
    ventana.title("Ventana Cpm")
    ventana.resizable(width=False,height=False)
    ##

    ## Lista de actividades.
    lista=Listbox(ventana)
    lista.place(x=20,y=10)
    lista.config(width=50,font=("Arial",12))
    ##
    ###Funciones
    def graficar():
        create_graph(get_critical_path(cpm_algorithm(data)),data)
    ###
    
    ### Botones

    ## Boton para mostrar grafo co ruta critica
    boton_grafo=Button(ventana,text="Mostrar Grafo con ruta crítica",font=("Arial",11),command=graficar)
    boton_grafo.place(x=160,y=230)
    boton_grafo.config(width=22,height=2)
    ##


    ####Ejecucion al abrir la ventana
    data=order_data(data)
    for node in cpm_algorithm(data):
        str2 ="Actividad: {}  ||Earty Start: {}||  Early finish: {}||  Late Start: {}||  Late finish: {}".format(
            node["activity"], node["es"], node["ef"], node["ls"], node["lf"]
        )
        lista.insert(END,str2)
        lista.insert(END,"")

    ####