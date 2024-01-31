from datetime import datetime
class Fichero:
    id = 0
    def __init__(self,id,nombre,tamaño,extension,contenido,fecha_creacion,fecha_modificacion):
        self.id = id
        self.nombre = nombre
        self.tamano = tamaño
        self.extension = extension
        self.contenido = contenido
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
    

    def __str__(self) -> str:
        return f"        Nombre: {self.nombre}, tamaño: {self.tamano},fecha modificacion: {self.fecha_modificacion}, fecha creacion: {self.fecha_creacion}"
        
    
    
    
