# Modulo de Gestion de Archivos en Memoria

from estructuras import Pila

class NodoArchivo:
    """Nodo doblemente enlazado que representa un archivo abierto."""
    def __init__(self, nombre, contenido=""):
        self.nombre = nombre
        self.contenido = contenido
        self.siguiente = None
        self.anterior = None
        # Pilas de Undo/Redo independientes por archivo
        self.pila_undo = Pila()
        self.pila_redo = Pila()


class ListaArchivos:
    """Lista enlazada doble para administrar los archivos de la sesion."""
    def __init__(self):
        self.cabeza = None
        self.activo = None

    def crear_archivo(self, nombre, contenido=""):
        nuevo = NodoArchivo(nombre, contenido)
        if not self.cabeza:
            self.cabeza = nuevo
            self.activo = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
            self.activo = nuevo
        return nuevo

    def listar(self):
        actual = self.cabeza
        if not actual:
            print("No hay archivos abiertos en la sesión.")
            return
        print("\n--- Archivos Abiertos ---")
        pos = 1
        while actual:
            estado = " (Activo)" if actual == self.activo else ""
            print(f"{pos}. {actual.nombre}{estado}")
            actual = actual.siguiente
            pos += 1

    def cambiar_activo(self, identificador):
        actual = self.cabeza
        pos = 1
        while actual:
            if str(pos) == str(identificador) or actual.nombre == identificador:
                self.activo = actual
                print(f"[✓] Archivo activo cambiado a: {actual.nombre}")
                return
            actual = actual.siguiente
            pos += 1
        print(f"[!] No se encontró el archivo '{identificador}'.")

    def eliminar(self, identificador):
        actual = self.cabeza
        pos = 1
        while actual:
            if str(pos) == str(identificador) or actual.nombre == identificador:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior

                if self.activo == actual:
                    self.activo = self.cabeza

                print(f"[✓] Archivo '{actual.nombre}' cerrado y liberado de memoria.")
                return
            actual = actual.siguiente
            pos += 1
        print(f"[!] No se encontró el archivo '{identificador}'.")