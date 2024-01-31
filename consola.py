from datetime import datetime
from json_manager import *
from Comando import Comando

def consola():
    root = cargarDatos()
    #Defino los parametros de ordenamiento
    ordenamiento_por = ["act","tam","fecha","ran",">","<"]
    while True:
        print(f"""
    -----------------------------------------------------------------------------------------------
    Comandos:
    dir   --listado de archivos y directorios
    help --Mostrar comandos de ordenacion
    -----------------------------------------------------------------------------------------------
    """)
        

        opcion = input("")

        if opcion == "dir":
            comando = Comando(opcion,"listar","usuario")
            comando._dir(root)
        elif opcion == "help":
             print("""
    Modo de uso:
    dir nombre_directorio ordenamiento_por modo_ordenamiento
    
    Ejemplos:
    1. dir carpeta act asc
       (Listar archivos de la carpeta 'carpeta' ordenados por fecha de modificación de forma ascendente)
       
    2. dir documentos tam des
       (Listar archivos de la carpeta 'documentos' ordenados por tamaño de forma descendente)
       
    3. dir fotos fecha asc
       (Listar archivos de la carpeta 'fotos' ordenados por fecha de forma ascendente)
       
    4. dir videos ran 5 10 asc
       (Listar archivos de la carpeta 'videos' con tamaño entre 5 y 10 ordenados por rango de forma ascendente)
       
    5. dir musica > 100
       (Listar archivos de la carpeta 'musica' con tamaño mayor a 100 ordenados por heapsort)
       
    6. dir descargas < 50
       (Listar archivos de la carpeta 'descargas' con tamaño menor a 50 ordenados por heapsort)
    """)
        
        else:
            opcion =  opcion.split(' ')
            carpetas = {}

            for almacenamiento in root:
                for carpeta in almacenamiento.lista:
                    carpetas[carpeta.nombre] = carpeta 


            if opcion[0] == "dir" and len(opcion) <=6:
                if opcion[1] in carpetas:
                    if opcion[2] in ordenamiento_por:

                        if opcion[2] ==  "act" and opcion[3] == "asc":
                            comando = Comando("ascendente","ordenar con mergesort","administrador")
                            resultado = comando.mergesort(carpetas[opcion[1]].lista)
                            for x in resultado:
                                print(x)    
                        elif opcion[2] == "act" and opcion[3] == "des":
                            comando = Comando("descendente","ordenar con mergesort","administrador")
                            resultado = comando.mergesort(carpetas[opcion[1]].lista)
                            for x in resultado:
                                print(x)   


                        elif opcion[2] == "tam" and opcion[3] == "asc":
                            comando = Comando("ascendente","ordenar con quicksort","administrador")
                            resultado = comando.quicksort(carpetas[opcion[1]].lista)
                            for x in resultado:
                                print(x) 

                        elif opcion[2] == "tam" and opcion[3] == "des":
                            comando = Comando("descendente","ordenar con quicksort","administrador")
                            resultado = comando.quicksort(carpetas[opcion[1]].lista)
                            for x in resultado:
                                print(x) 


                        elif opcion[2] == "fecha" and opcion[3] == "asc":
                            comando = Comando("ascendente","ordenar fecha","administrador")
                            resultado = comando.mergesort(carpetas[opcion[1]].lista)
                            for x in resultado:
                                print(x)


                        elif opcion[2] == "fecha" and opcion[3] == "des":
                            comando = Comando("descendente","ordenar fecha","administrador")
                            resultado = comando.mergesort(carpetas[opcion[1]].lista)
                            for x in resultado:
                                print(x)


                        elif opcion[2] == "ran" and len(opcion) == 6:
                            try:
                                rango1 = int(opcion[3])
                                rango2 = int(opcion[4])

                                if rango1 >= rango2:
                                    print("El limite mayor no puede ser menor")
                                else:
                                    if  opcion[5]=="asc":
                                        comando = Comando("rango","ascendente","administrador")
                                        resultado = comando.shellsort(carpetas[opcion[1]].lista,rango1,rango2)
                                        for x in resultado:
                                            print(x)


                                    elif opcion[5] == "des":
                                        comando = Comando("rango","descendente","administrador")
                                        resultado = comando.shellsort(carpetas[opcion[1]].lista,rango1,rango2)
                                        for x in resultado:
                                            print(x)

                                        

                                    else:
                                        print("Solo admitido asc y des")
                                    
                            except Exception as e:
                                print(e)


                        elif opcion[2] == ">" and len(opcion) == 4:
                            try:
                                mayor = int(opcion[3])
                                comando = Comando("mayor","ordenamiento heapsort","administrador")
                                resultado = comando.heapsort_recursive(carpetas[opcion[1]].lista,mayor)
                                for x in resultado:
                                    print(x)
                            except Exception as e:
                                print(e)


                        elif opcion[2] == "<" and len(opcion) == 4:
                            try:
                                menor = int(opcion[3])
                                comando = Comando("menor","ordenamiento heapsort","administrador")
                                resultado = comando.heapsort_recursive(carpetas[opcion[1]].lista,menor)
                                for x in resultado:
                                    print(x)
                            except:
                                print("Error, limite no admitido")                                
 
 
 
 
 
 
 
                        else:    
                            print("Error, comando no valido")
                            
                    else:
                        print("Error,  no es un parametro valido.")
                else:
                    print("Error, la carpeta no existe.")
            
            else:
                print("Error comando no valido")



            
                
            
