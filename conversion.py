import csv
from tkinter import messagebox

class convertidor:
   
    def __init__(self):
      pass

    def limpiar_texto(self,columna):
        reemplazos = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
            'ñ': 'n', 'Ñ': 'N', '°' : 'ro', 'º' : 'ro', 'Ü' : 'U',
            'Ò' : 'O', 'ò' : 'o', 'ü' : 'U', 'è' : 'e', 'È':'E', 'â' : 'a', 'ê' : 'e',
            'À' : 'A', 'Ì' : 'I', 'Ù' : 'U','à' : 'a', 'è' :'e','ì': 'i', 'ù' : 'u',
            'Û' : 'U', 'Â' : 'A', 'Ö' : 'O'
            }
        
        for a, b in reemplazos.items():
            columna = columna.replace(a, b)
        
        return columna
    
    
    def delimitador(self, archivo):
        try:
         with open(archivo, 'r', encoding='utf-8') as entrada:
            muestra = entrada.read(3072)  
            sniffer = csv.Sniffer()
            delimitador = sniffer.sniff(muestra).delimiter  
         return delimitador
        except csv.Error:
            return ';'


    def limpiarnombres(self, fila,columna):
       reemplazos = {
            "'" : ' ', '`' : ' ','_': ' ', '-' : ' ', ','  : ' ', '.': ' ', '*' : ' ','/ ' : ' '
            }
        
       for a, b in reemplazos.items():
            fila[columna] = fila[columna].replace(a, b)
            #fila[2] = fila[2].replace(a, b)

        
       return fila


    def convertir(self,entradacsv,salidacsv):
     delimitador = self.delimitador(entradacsv)
     try:
        with open(entradacsv, 'r', encoding='utf-8') as entrada:
            lector = csv.reader(entrada, delimiter=delimitador, quotechar='"', skipinitialspace=True)  
            with open(salidacsv,'w', newline='', encoding='utf-8') as salida:
             escritor = csv.writer(salida, delimiter=delimitador, quotechar='"', quoting=csv.QUOTE_MINIMAL)

             for fila in lector:
                fila1 = [self.limpiar_texto(campo) for campo in fila] 
                #fila1 = self.limpiarnombres(fila1)
                escritor.writerow(fila1)
     except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")


    def convertirnombre(self,entradacsv,salidacsv,columna):
     delimitador = self.delimitador(entradacsv)
     try:
        with open(entradacsv, 'r', encoding='utf-8') as entrada:
            lector = csv.reader(entrada, delimiter=delimitador, quotechar='"', skipinitialspace=True)  
            with open(salidacsv,'w', newline='', encoding='utf-8') as salida:
             escritor = csv.writer(salida, delimiter=delimitador, quotechar='"', quoting=csv.QUOTE_MINIMAL)  
             for fila in lector:
                if len(fila) > columna:
                 fila1= fila
                 fila1= self.limpiarnombres(fila1,columna)
                 escritor.writerow(fila1) 
                else:
                 messagebox.showerror('Error, indice de columna inexistente')              
     except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")         

