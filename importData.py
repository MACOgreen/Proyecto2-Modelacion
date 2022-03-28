from tkinter import Label,Tk, filedialog, Button

def importDataFunction(route):
    # Cargar todas las líneas del archivo
    file = open(route, 'r')
    lines = file.readlines()
    lines.pop(0) #Se elimina el encabezado
    file.close()

    # Procesar data y guardar en estructuras de datos
    data =[]
    for line in lines:
        columns = line.split("|", 3)
        columns[0] = columns[0].strip()
        columns[2] = columns[2].strip()
        columns[3] = columns[3].strip()
        data.append({
            "activity": columns[0],
            "description": columns[1],
            "duration": int(columns[2]),
            "predecessors":[number for number in columns[3].split(",") if columns[3] != "--"],
            "es":0,
            "ef":0,
            "ls":0,
            "lf":0,
        })

    return data


