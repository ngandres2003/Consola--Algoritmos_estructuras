class Almacenamiento:
    def __init__(self,id,nombre,capacidad_total,capacidad_disponible,tipo,lista_directorio):
        self.id = id
        self.nombre = nombre
        self.capacidad_total = capacidad_total
        self.espacio_disponible = capacidad_disponible
        self.tipo = tipo
        self.lista = lista_directorio
    
    def listar(self):
        for x in self.lista:
            print(x)
            x.listar()
            

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Capacidad total: {self.capacidad_total}, Espacio Disponible: {self.espacio_disponible}"     