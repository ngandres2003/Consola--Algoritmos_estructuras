import json
import os
from Fichero import Fichero
from Directorio import Directorio
from Almacenamiento import Almacenamiento

def read_json():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            return data
    except:
        print("Error leyendo archivo .json")

def cargarDatos():
    try:
        data = read_json()
        almacenamiento_lista = []

        for almacenamiento in data:
            almacenamiento_id = almacenamiento["almacenamiento_id"]
            almacenamiento_nombre = almacenamiento["nombre"]
            almacenamiento_capacidad = almacenamiento["capacidad_total"]
            almacenamiento_disponible = almacenamiento["capacidad_disponible"]
            almacenamiento_tipo = almacenamiento["tipo"]
            almacenamiento_lista_directorio = almacenamiento["lista_directorio"]
            directorio_lista = []

            for directorio in almacenamiento_lista_directorio:
                directorio_id = directorio["directorio_id"]
                directorio_nombre = directorio["nombre"]
                directorio_fecha_creacion = directorio["fecha_creacion"]
                directorio_lista_ficheros = directorio["lista_ficheros"]
                fichero_lista = []

                for fichero in directorio_lista_ficheros:
                    fichero_id = fichero["fichero_id"]
                    fichero_nombre = fichero["nombre"]
                    fichero_tamaño = fichero["tamano"]
                    fichero_extension = fichero["extension"]
                    fichero_contenido = fichero["contenido"]
                    fichero_fecha_creacion = fichero["fecha_creacion"]
                    fichero_fecha_modificacion = fichero["fecha_modificacion"]
                    aux_fichero = Fichero(fichero_id,fichero_nombre,fichero_tamaño,fichero_extension,fichero_contenido,fichero_fecha_creacion,fichero_fecha_modificacion)
                    fichero_lista.append(aux_fichero)
                
                aux_directorio = Directorio(directorio_id,directorio_nombre,fichero_lista,directorio_fecha_creacion)
                directorio_lista.append(aux_directorio)
            
            aux_almacenamiento = Almacenamiento(almacenamiento_id,almacenamiento_nombre,almacenamiento_capacidad,almacenamiento_disponible,almacenamiento_tipo,directorio_lista)
            almacenamiento_lista.append(aux_almacenamiento)  

        return almacenamiento_lista 
    except Exception as error:
        print(error)
   
        
