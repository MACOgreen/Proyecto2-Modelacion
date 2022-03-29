from tkinter import *
from cpm import (
    cpm_algorithm,
    get_critical_path,
    create_graph,
    order_data,
    create_graph_simple,
)


def just_graph(data):
    ordered_list = order_data(data.copy())
    create_graph_simple(ordered_list)


def cpm(data):
    ordered_list = order_data(data.copy())
    ventana = Tk()
    ##Configuracion la ventana
    ventana.geometry("652x300+500+190")
    ventana.title("Ventana Cpm")
    ventana.resizable(width=False, height=False)
    ##

    ## Lista de actividades.
    lista = Listbox(ventana)
    lista.place(x=9, y=10)
    lista.config(width=70, font=("Arial", 12))
    ##
    ###Funciones
    def graficar():
        cpm = cpm_algorithm(ordered_list)
        create_graph(get_critical_path(cpm), ordered_list)

    ###

    ### Botones

    ## Boton para mostrar grafo co ruta critica
    boton_grafo = Button(
        ventana,
        text="Mostrar Grafo con ruta crítica",
        font=("Arial", 11),
        command=graficar,
    )
    boton_grafo.place(x=221, y=230)
    boton_grafo.config(width=22, height=2)
    ##

    ####Ejecucion al abrir la ventana
    for node in cpm_algorithm(ordered_list):
        holgura = node["ls"] - node["es"]
        str2 = "Actividad: {}  ||Earty Start: {}||  Early finish: {}||  Late Start: {}||  Late finish: {}|| Holgura: {}".format(
            node["activity"], node["es"], node["ef"], node["ls"], node["lf"],holgura
        )
        lista.insert(END, str2)
        lista.insert(END, "")

    ####
