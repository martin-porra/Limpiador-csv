import csv 
from datetime import datetime
    
def detectarÃ():     
 with open('Migracion.csv', 'r', encoding='ISO-8859-1') as archivo:
    lector = csv.reader(archivo, delimiter=';', quotechar='"', skipinitialspace=True) 
    lista = []
    for fila in lector:
        for campo in fila:
         if isinstance(campo,str):
          if 'Ã' in campo:
            lista.append(campo)
 print(lista)   

def detectarcaracteresnombre(num):     
 with open('Migracion2.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo, delimiter=';', quotechar='"', skipinitialspace=True) 
    lista = []
    for fila in lector:
        if not fila[num].replace(" ", "").isalpha():
            lista.append(fila[num])
 print(lista)   


def esnumero(campo):
    with open('Migracion2.csv', 'r', encoding='utf-8') as archivo:
      lector = csv.reader(archivo, delimiter=';', quotechar='"', skipinitialspace=True) 
      lista = []
      for fila in lector:
        if any(char not in "0123456789" for char in fila[campo]):
            lista.append(fila[campo])
    print(lista)   

def NoVacioint(campo):      
  with  open('Migracion2.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo, delimiter=';',quotechar='"', skipinitialspace=True)
    lista = []
    for indice,fila in enumerate(lector):
     if fila[campo] == '' or fila[campo] is None or fila[campo].strip().lower() == 'vacio' or  not fila[campo].isdigit():
        lista.append(indice+1)
  print(lista)

def NoVaciostr(campo):      
   with  open('Migracion2.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo, delimiter=';',quotechar='"', skipinitialspace=True)
    lista = []
    for indice,fila in enumerate(lector):
     if  fila[campo] == '' or fila[campo] is None or fila[campo].strip().lower() == 'vacio' or  not fila[campo].replace(" ", "").isalpha():
        lista.append(indice+1)
   print(lista)



def unico():
    with open('Migracion2.csv', 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter=';', quotechar='"', skipinitialspace=True)
        dnis = {}
        for fila in lector:
            dni = fila[4]
            nombre = fila[1]
            if dni in dnis:
                if nombre not in dnis[dni]:
                    dnis[dni].append(nombre)
            else:
                dnis[dni] = [nombre]
    dnis_duplicados = {dni: nombres for dni, nombres in dnis.items() if len(nombres) > 1}
    for dni, nombres in dnis_duplicados.items():
        print(f"DNI: {dni} - Nombres: {', '.join(nombres)}")
    


def encontrar(): 
 with open('Migracion2.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo, delimiter=';', quotechar='"', skipinitialspace=True)
    for fila in lector:
       if fila[3] != '1':
          print(fila[3])




def esfecha(formato='%d/%m/%Y'): 
        with open('Migracion2.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=';', quotechar='"', skipinitialspace=True)
            next(lector) 
            for indice, fila in enumerate(lector, start=2):  
                    try:
                        if fila[5].strip():  
                            datetime.strptime(fila[5].strip(), formato)
                        else:
                            print(f" La fecha en la fila {indice} está vacía")
                    except ValueError:
                        print(f'Error de formato en la fila {indice}: "{fila[5]}" no es una fecha válida')
                        return False


if __name__=='__main__':
 #NoVacioint(4)  
 #NoVaciostr(3)
 #detectarÃ()
 #unico()   
 #detectarcaracteresnombre(2)
 #encontrar()
 #esnumero(4)
 esfecha('%d/%m/%Y')