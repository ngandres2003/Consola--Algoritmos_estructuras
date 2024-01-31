from datetime import datetime
class Directorio:
    def __init__(self,id,nombre,lista_ficheros,fecha_creacion):
        self.id = id
        self.nombre = nombre
        self.lista = lista_ficheros
        self.fecha_creacion = fecha_creacion

    def listar(self):
        for x in self.lista:
            print(x)
        print()

    def tamaño(self):
        return len(self.lista_ficheros)
    
    def __str__(self) -> str:
        return f"    Nombre: {self.nombre}, fecha creacion: {self.fecha_creacion}"