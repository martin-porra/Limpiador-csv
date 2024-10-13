import tkinter as tk
from tkinter import filedialog, font, Toplevel, messagebox
from tooltip import ToolTip 
from conversion import convertidor

def procesar_dato(ventana, entrada, salida,columna,convertidor):
    try:
     dato = int(columna.get())
     convertidor.convertirnombre(entrada,salida, (dato-1))
     ventana.destroy()
    except ValueError:
      messagebox.showerror("Error", "El valor ingresado debe ser un número entero")

# Función que abre una ventana secundaria para ingresar un dato
def abrir_ventana(entrada,salida,convertidor):
    ventana_secundaria = Toplevel()  
    ventana_secundaria.title("Ingresar Dato")
    ventana_secundaria.geometry("300x100")

    label = tk.Label(ventana_secundaria, text="Ingrese un dato:")
    label.pack(pady=5)

    columna = tk.Entry(ventana_secundaria)  
    columna.pack(pady=5)

    boton_aceptar = tk.Button(ventana_secundaria, text="Aceptar", command=lambda: procesar_dato(ventana_secundaria, entrada,salida,columna,convertidor))
    boton_aceptar.pack(pady=5)


def seleccionar_archivo_entrada():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if archivo:  
        entradacsv.delete(0, tk.END)  
        entradacsv.insert(0, archivo)


if __name__ == '__main__':
    convertidor = convertidor()
    ventana = tk.Tk()
    ventana.title("Eliminar símbolos CSV")
    ventana.geometry("480x200")
    
    label_entrada = tk.Label(ventana, text="Archivo de entrada:")
    label_entrada.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    entradacsv = tk.Entry(ventana, width=50)
    entradacsv.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    boton_seleccionar_entrada = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo_entrada)
    boton_seleccionar_entrada.grid(row=2, column=3, padx=10, pady=5)

    label_salida = tk.Label(ventana, text="Archivo de salida:")
    label_salida.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    salidacsv = tk.Entry(ventana, width=50)
    salidacsv.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    botonLimpiar = tk.Button(ventana, text="Limpiar archivo", command=lambda: 
        convertidor.convertir(
            entradacsv.get() + (".csv" if not entradacsv.get().endswith(".csv") else ""),
            salidacsv.get() + (".csv" if not salidacsv.get().endswith(".csv") else "")
        )
    )
    botonLimpiar.grid(row=4, column=0, padx=10, pady=10)
    ToolTip1= ToolTip(botonLimpiar, 'Elimina los acentos,Ñ, de todo el archivo CSV')
    botonnombre = tk.Button(ventana, text='Limpiar Nombre', command=lambda:
        abrir_ventana(
            entradacsv.get() + (".csv" if not entradacsv.get().endswith(".csv") else ""),
            salidacsv.get() + (".csv" if not salidacsv.get().endswith(".csv") else ""),convertidor
        ))
    botonnombre.grid(row=4, column=1, padx=10, pady=10)
    ToolTip2 = ToolTip(botonnombre, 'Ingrese el numero de columna para eliminar simbolos (.,;-_)de la columna nombre')


    botonsalir = tk.Button(ventana, text="Salir", command=ventana.quit)
    botonsalir['font'] = font.Font(size=9) 
    botonsalir.grid(row=4, column=2,columnspan=2, padx=20, pady=20, sticky="nsew")
    

    ventana.mainloop()