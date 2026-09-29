# Modulo Principal del Entorno IDE (Synthetix Studio)

import json
from estructuras import Pila, Cola
from archivo import ListaArchivos
from ordenamiento import MotorOrdenamiento

class SynthetixStudio:
    """Clase controladora del Mini IDE."""
    def __init__(self):
        self.archivos = ListaArchivos()
        self.buffer_ia = Cola()
        self.config = {}

        # Cargar archivos por defecto para pruebas
        self._cargar_datos_defecto()

    def _cargar_datos_defecto(self):
        """Carga datos de prueba iniciales."""
        self.archivos.crear_archivo(
            "sistema_ferroviario.py",
            "class Tren:\n    def __init__(self):\n        self.vagones = {1, 2, 3"  # Error intencional en linea 3 para probar la Pila
        )
        self.archivos.crear_archivo(
            "clientes.py",
            "def buscar_cliente(id_cliente):\n    return hash_table.get(id_cliente)"
        )

    def cargar_configuracion(self, ruta_archivo):
        """Lee el archivo de configuracion JSON externo."""
        try:
            with open(ruta_archivo, 'r') as f:
                self.config = json.load(f)
            print(f"[✓] Configuracion cargada desde: {ruta_archivo}")
        except FileNotFoundError:
            print(f"[!] Archivo '{ruta_archivo}' no encontrado.")
        except json.JSONDecodeError:
            print(f"[!] Formato JSON inválido.")

    def verificar_sintaxis(self):
        """Valida () [] {} usando la Pila."""
        if not self.archivos.activo:
            print("[!] No hay ningún archivo activo.")
            return

        codigo = self.archivos.activo.contenido
        pila_delimitadores = Pila()
        pares = {')': '(', ']': '[', '}': '{'}

        for num_linea, linea in enumerate(codigo.split('\n'), 1):
            for char in linea:
                if char in "([{":
                    pila_delimitadores.apilar((char, num_linea))
                elif char in ")]}":
                    if pila_delimitadores.esta_vacia():
                        print(f"[!] Error: Símbolo '{char}' inesperado en línea {num_linea}.")
                        return
                    tope, linea_origen = pila_delimitadores.desapilar()
                    if pares[char] != tope:
                        print(f"[!] Error: Se esperaba cerrar '{tope}' (línea {linea_origen}), pero se halló '{char}' en línea {num_linea}.")
                        return

        if not pila_delimitadores.esta_vacia():
            tope, linea_origen = pila_delimitadores.desapilar()
            print(f"[!] Error: Símbolo '{tope}' de la línea {linea_origen} no fue cerrado.")
        else:
            print("[✓] Sintaxis correcta: Delimitadores balanceados.")

    def editar_contenido(self, nuevo_texto):
        """Modifica el codigo activo guardando el estado previo en Undo."""
        if not self.archivos.activo:
            print("[!] No hay archivo activo para editar.")
            return

        self.archivos.activo.pila_undo.apilar(self.archivos.activo.contenido)
        self.archivos.activo.contenido = nuevo_texto
        self.archivos.activo.pila_redo = Pila()  # Limpia Redo al realizar un nuevo cambio
        print("[✓] Modificación guardada en el historial.")

    def deshacer(self):
        """Deshace el ultimo cambio (Undo)."""
        archivo = self.archivos.activo
        if archivo and not archivo.pila_undo.esta_vacia():
            archivo.pila_redo.apilar(archivo.contenido)
            archivo.contenido = archivo.pila_undo.desapilar()
            print("[✓] Cambio deshecho (Undo).")
        else:
            print("[!] No hay cambios para deshacer.")

    def rehacer(self):
        """Rehace el cambio previamente deshecho (Redo)."""
        archivo = self.archivos.activo
        if archivo and not archivo.pila_redo.esta_vacia():
            archivo.pila_undo.apilar(archivo.contenido)
            archivo.contenido = archivo.pila_redo.desapilar()
            print("[✓] Cambio rehecho (Redo).")
        else:
            print("[!] No hay cambios para rehacer.")

    def solicitar_analisis_ia(self):
        """Encola peticiones de analisis en el buffer FIFO."""
        if not self.archivos.activo:
            print("[!] No hay archivo activo.")
            return

        nombre = self.archivos.activo.nombre
        self.buffer_ia.encolar(f"Analizar complejidad Big-O de: {nombre}")
        print(f"[✓] Petición para '{nombre}' encolada en el buffer FIFO.")

    def estado_cola(self):
        """Muestra el estado actual del buffer de peticiones."""
        peticiones = self.buffer_ia.ver_estado()
        if not peticiones:
            print("El buffer de peticiones IA está vacío.")
        else:
            print("\n--- Buffer de Peticiones IA (FIFO) ---")
            for idx, item in enumerate(peticiones, 1):
                print(f"  {idx}. {item}")

    def ordenar_diagnosticos(self, criterio, algoritmo):
        """Genera y ordena diagnósticos con Mergesort."""
        diagnosticos = [
            {"line": 45, "gravedad": 3, "msg": "Variable no utilizada 'x'"},
            {"line": 3,  "gravedad": 1, "msg": "Llave de cierre faltante"},
            {"line": 22, "gravedad": 2, "msg": "Complejidad ciclomática alta en función"}
        ]

        crit = "line" if criterio in ["line", "linea"] else "gravedad"

        if algoritmo == "mergesort":
            resultado = MotorOrdenamiento.mergesort(diagnosticos, crit)
            print(f"\n--- Diagnósticos Ordenados por {crit.upper()} ({algoritmo}) ---")
            for d in resultado:
                print(f"Línea {d['line']:02d} | Gravedad: {d['gravedad']} | {d['msg']}")
        else:
            print(f"[!] Algoritmo '{algoritmo}' no reconocido. Usa 'mergesort'.")