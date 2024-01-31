import time
class Comando:
    id = 0
    roles = ["usuario","administrador"]
    
    def __init__(self,nombre,descripcion,rol):
        Comando.id += 1
        self.id = Comando.id
        self.nombre = nombre
        self.descripcion = descripcion
        #Verifica si el rol pasado es valido
        if  rol in Comando.roles:
            self.rol = rol
        else:
            raise ValueError("El rol no es valido")

    #Lista todos los datos 
    def _dir(self,root):
            for almacenamiento in root:
                print(almacenamiento)
                almacenamiento.listar()

    #Ordena y lista ficheros de una carpeta mediante quicksort ascendentemente segun su tamano
    def quicksort(self,carpeta):
        if len(carpeta) <= 1:
            return carpeta
        else:
            pivot = carpeta[0]
            if self.nombre == "ascendente":
                menores = [elemento for elemento in carpeta[1:] if int(elemento.tamano) <= int(pivot.tamano)]
                mayores = [elemento for elemento in carpeta[1:] if int(elemento.tamano) > int(pivot.tamano)]
            else:
                menores = [elemento for elemento in carpeta[1:] if int(elemento.tamano) >= int(pivot.tamano)]
                mayores = [elemento for elemento in carpeta[1:] if int(elemento.tamano) < int(pivot.tamano)]
            return self.quicksort(menores) + [pivot] + self.quicksort(mayores)

    
    #Ordena y lista ficheros de una carpeta mediante mergesort ascendentemente segun su modificacion
    def mergesort(self,carpeta):
        if len(carpeta) <= 1:
            return carpeta

        # Dividir la lista en dos mitades
        mitad = len(carpeta) // 2
        izquierda = carpeta[:mitad]
        derecha = carpeta[mitad:]

        # Llamadas recursivas para ordenar cada mitad
        izquierda = self.mergesort(izquierda)
        derecha = self.mergesort(derecha)

        # Combinar las dos mitades ordenadas
        return self.merge(izquierda, derecha)

    def merge(self,izquierda, derecha):
        resultado = []
        i = j = 0
        #Verificar modo de ordenamiento
        if self.nombre == "ascendente":
            while i < len(izquierda) and j < len(derecha):
                #Verificar la fecha a ordenar
                if self.descripcion == "ordenar fecha":
                    f1 = time.strptime(izquierda[i].fecha_creacion,"%m/%d/%Y")
                    f2 = time.strptime(derecha[j].fecha_creacion,"%m/%d/%Y")
                else:
                    f1 = time.strptime(izquierda[i].fecha_modificacion,"%m/%d/%Y")
                    f2 = time.strptime(derecha[j].fecha_modificacion,"%m/%d/%Y")
                if f1 < f2:
                    resultado.append(izquierda[i])
                    i += 1
                else:
                    resultado.append(derecha[j])
                    j += 1
        else:
            while i < len(izquierda) and j < len(derecha):
                if self.descripcion == "ordenar fecha":
                    f1 = time.strptime(izquierda[i].fecha_creacion,"%m/%d/%Y")
                    f2 = time.strptime(derecha[j].fecha_creacion,"%m/%d/%Y")
                else:
                    f1 = time.strptime(izquierda[i].fecha_modificacion,"%m/%d/%Y")
                    f2 = time.strptime(derecha[j].fecha_modificacion,"%m/%d/%Y")

                if f1 > f2:
                    resultado.append(izquierda[i])
                    i += 1
                else:
                    resultado.append(derecha[j])
                    j += 1

        # Agregar los elementos restantes de ambas listas
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado

    def shell_sort_recursive(self,arr, gap):
        n = len(arr)

        if gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                if self.descripcion == "ascendente":
                    while j >= gap and int(arr[j - gap].tamano) > int(temp.tamano):
                        arr[j] = arr[j - gap]
                        j -= gap
                else:
                    while j >= gap and int(arr[j - gap].tamano) < int(temp.tamano):
                        arr[j] = arr[j - gap]
                        j -= gap

                arr[j] = temp

            self.shell_sort_recursive(arr, gap // 2)



    def shellsort(self,carpeta,rango1,rango2):

        arr = self.rango(carpeta,rango1,rango2)
        n = len(arr)
        gap = n // 2
        self.shell_sort_recursive(arr, gap)
        return arr
    

    def rango(self,carpeta,rango1,rango2):
        arr = []

        for x in carpeta:

            if int(x.tamano) >=  rango1 and int(x.tamano) <= rango2:
                arr.append(x)
        return arr
    

    def heapify(self,arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and int(arr[left].tamano) > int(arr[largest].tamano):
            largest = left

        if right < n and int(arr[right].tamano) > int(arr[largest].tamano):
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapsort_recursive(self,carpeta,rango):
        arr = self.mayor_menor(carpeta,rango)
        n = len(arr)

        # Construir un max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extraer elementos uno por uno del heap
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
        return arr
    
    def mayor_menor(self,carpeta,n):
        arr = []
        if self.nombre == "mayor":
            for x in carpeta:
                if int(x.tamano) >= n:
                    arr.append(x)
        else:
            for x in carpeta:
                if int(x.tamano) <= n:
                    arr.append(x)
        return arr