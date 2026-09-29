La lógica está organizada dentro del directorio `src/` en los siguientes módulos:

- `estructuras.py`: Contiene las clases `Nodo`, `Pila` (LIFO) y `Cola` (FIFO) creadas con punteros enlazados.
- `archivo.py`: Implementa `ListaArchivos` (lista doblemente enlazada) y `NodoArchivo` para la gestión de archivos abiertos y su historial propio de cambios.
- `ordenamiento.py`: Clase `MotorOrdenamiento` con el algoritmo Mergesort implementado de forma manual.
- `ide.py`: Clase `SynthetixStudio` que integra la lectura de `config.json`, la verificación de sintaxis, el control de cambios y el buffer de la IA.
- `main.py`: Punto de entrada que ejecuta la consola de comandos (CLI).

1. Estructuras dinámicas
- Pila: $\mathcal{O}(1)$ en tiempo. Las operaciones modifican únicamente la referencia en el tope.
- Cola: $\mathcal{O}(1)$ en tiempo. Se utilizan punteros directos al frente y al final para operar en tiempo constante.
- Lista Doblemente Enlazada: Búsquedas por nombre o posición en $\mathcal{O}(n)$. Modificación y reconexión de punteros en $\mathcal{O}(1)$.

2. Verificación de sintaxis (`check`)
- Tiempo: $\mathcal{O}(n)$, donde $n$ es la cantidad de caracteres en el archivo activo. Realiza un único recorrido almacenando y validando delimitadores en la pila en tiempo constante.
- Espacio $\mathcal{O}(m)$, siendo $m$ el número de símbolos de agrupación abiertos en memoria.

3. Ordenamiento (Mergesort)
- Tiempo: $\mathcal{O}(n \log n)$ en el mejor, peor y promedio de los casos. Divide el arreglo recursivamente en $\mathcal{O}(\log n)$ niveles y realiza la mezcla en $\mathcal{O}(n)$ por nivel.
- Espacio: $\mathcal{O}(n)$ debido a las sublistas auxiliares requeridas durante la fusión de arreglos.

Cómo ejecutar
1. Para iniciar el entorno desde la terminal:
   python src/main.py

2. Para cargar el archivo de configuración externo dentro del CLI:
   config config.json
