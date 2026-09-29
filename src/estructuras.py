# Modulo de Estructuras de Datos Lineales

class Nodo:
    """Nodo simple para Pilas y Colas."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    """Estructura LIFO propia con nodos enlazados."""
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def desapilar(self):
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def esta_vacia(self):
        return self.tope is None


class Cola:
    """Estructura FIFO propia para el buffer de peticiones."""
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato

    def esta_vacia(self):
        return self.frente is None

    def ver_estado(self):
        """Devuelve los elementos de la cola para visualización."""
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos