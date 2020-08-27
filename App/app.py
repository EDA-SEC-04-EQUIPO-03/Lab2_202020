"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar elementos a partir de criterio")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria1, criteria2, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    if lst['size']==0:
        print("La lista esta vacía")
        return 0
    else:
        print("proceso 1")
        t1_start = process_time()
        iterator = it.newIterator(lst)
        p10_mejores=[0,0,0,0,0,0,0,0,0,0]
        while  it.hasNext(iterator):
            element= it.next(iterator)
            if criteria.lower() in element[column1].lower(): "vote count = criteria"
                if elemento[columns1]>p10_mejores[0] and elemento[columns1] not in p10_mejores:
                    p10_mejores[0]=element[column2]
                if elemento[columns1]>p10_mejores[1] and elemento[columns1] not in p10_mejores:
                    p10_mejores[1]=element[column2]
                if elemento[columns1]>p10_mejores[2] and elemento[columns1] not in p10_mejores:
                    p10_mejores[2]=element[column2]
                if elemento[columns1]>p10_mejores[3] and elemento[columns1] not in p10_mejores:
                    p10_mejores[3]=element[column2]
                if elemento[columns1]>p10_mejores[4] and elemento[columns1] not in p10_mejores:
                    p10_mejores[4]=element[column2]
                if elemento[columns1]>p10_mejores[5] and elemento[columns1] not in p10_mejores:
                    p10_mejores[5]=element[column2]
                if elemento[columns1]>p10_mejores[6] and elemento[columns1] not in p10_mejores:
                    p10_mejores[6]=element[column2]
                if elemento[columns1]>p10_mejores[7] and elemento[columns1] not in p10_mejores:
                    p10_mejores[7]=element[column2]
                if elemento[columns1]>p10_mejores[8] and elemento[columns1] not in p10_mejores:
                    p10_mejores[8]=element[column2]
                if elemento[columns1]>p10_mejores[9] and elemento[columns1] not in p10_mejores:
                    p10_mejores[9]=element[column2]
        t1_stop = process_time()
        print("Tiempo de ejecución del proceso 1 ",t1_stop-t1_start," segundos")
        print("proceso 2")
        t2_start = process_time()
        iterator = it.newIterator(lst)
        promedios_malo=[11111111111,11111111111,11111111111,11111111111,11111111111] 
        while  it.hasNext(iterator): "vote average = criteria"
            element=it.next(iterator)
            if criteria2.lower() in element[columns2].lower():
                if elemento[columns2]<promedios_malo[0] and elemento[columns2] not in promedios_malo:
                    promedios_malo[0]=element[columns2]
                if elemento[columns2]<promedios_malo[1] and elemento[columns2] not in promedios_malo:
                    promedios_malo[1]=element[columns2]
                if elemento[columns2]<promedios_malo[2] and elemento[columns2] not in promedios_malo:
                    promedios_malo[2]=element[columns2]
                if elemento[columns2]<promedios_malo[3] and elemento[columns2] not in promedios_malo:
                    promedios_malo[3]=element[columns2]
                if elemento[columns2]<promedios_malo[4] and elemento[columns2] not in promedios_malo:
                    promedios_malo[4]=element[columns2]
        t2_stop = process_time()
        print("Tiempo de ejecución del proceso 2 ",t2_stop-t2_start," segundos")
    return (p10_mejores,promedios_malo)

def orderElementsByCriteria(nombre, lst):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if lst['size']==0:
        print("La lista esta vacía")
        return 0
    else:
        print("proceso 1")) "lista csv 2"
        lista_id=[]
        t1_start = process_time()
        iterator = it.newIterator(lst)
        num_pelis=0
        while  it.hasNext(iterator):
            element=it.next(iterador)
            if "director_name".lower() in element[column1].lower() and "id".lower() in element[column2]:
                for x in range (0,lst["zize"]):
                    if nombre in element[column1]:
                        num_pelis+=1
                        lista_id.append(element[column2])
        t1_stop = process_time()
        print("Tiempo de ejecución del proceso 1 ",t2_stop-t2_start," segundos")

        print("proceso 2") "lista csv 1"
        t2_start = process_time()
        lista_dirigidas=[]
        iterator = it.newIterator(lst)
        num_pelis=0
        if "vote_average".lower() in element[column1].lower() and "original_tittle".lower() in element[column2] and "id" in element[column0]:
        while  it.hasNext(iterator):
            element=it.next(iterador)
            for id in lista_id:
                if element[column0] == id:
                    promedio+=element[column1]
                    lista_dirigidas.append(element[column2])
        t2_stop = process_time()
        print("Tiempo de ejecución del proceso 2 ",t2_stop-t2_start," segundos")
    promedio_pelis=promedio/num_pelis
    return (lista_dirigidas, num_pelis, promedio_pelis)

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/test.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria1 =input('Ingrese el criterio de búsqueda #1\n')
                    criteria1 =input('Ingrese el criterio de búsqueda #2\n')
                    counter=countElementsByCriteria(criteria1, criteria2, lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria1, criteria2 ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    nombre =input('Ingrese el nombre del director\n')
                    counter=countElementsByCriteria(nombre, lst)
                    print("Coinciden ",counter," elementos con el director: '", nombre )
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()