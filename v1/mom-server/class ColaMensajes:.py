class ColaMensajes:
    def __init__(self):
        self.cola = []
        self.colas_por_usuario = {}

 

    def inserte_mensaje(self, comentario, usuario, nombre_cola):
        if not comentario:
            raise ValueError("El comentario no puede estar vacío")
        if not usuario:
            raise ValueError("El nombre de usuario no puede estar vacío")
        if not nombre_cola:
            raise ValueError("El nombre de la cola no puede estar vacío")

 

        mensaje = (usuario, nombre_cola, comentario)
        self.cola.append(mensaje)

 

        if usuario not in self.colas_por_usuario:
            self.colas_por_usuario[usuario] = {}
        if nombre_cola not in self.colas_por_usuario[usuario]:
            self.colas_por_usuario[usuario][nombre_cola] = []
        self.colas_por_usuario[usuario][nombre_cola].append(mensaje)

 

    def mensaje_siguiente(self):
        if not self.cola:
            return None
        mensaje = self.cola[0]
        self.cola.pop(0)
        usuario, nombre_cola, _ = mensaje
        self.colas_por_usuario[usuario][nombre_cola].pop(0)
        return mensaje