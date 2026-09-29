# Punto de Entrada Principal (CLI)

from ide import SynthetixStudio

def ejecutar_cli():
    ide = SynthetixStudio()
    print("=== Synthetix Studio (Mini IDE CLI) ===")
    print("Escribe 'help' para ver la lista de comandos disponibles.")

    while True:
        activo = ide.archivos.activo.nombre if ide.archivos.activo else "Ninguno"
        entrada = input(f"\n[{activo}] > ").strip()

        # Validacion de entrada vacia
        if not entrada:
            print("[!] La entrada no puede estar vacía.")
            continue

        partes = entrada.split()
        cmd = partes[0].lower()
        args = partes[1:]

        if cmd == "new":
            if args:
                ide.archivos.crear_archivo(args[0])
                print(f"[✓] Archivo '{args[0]}' creado.")
            else:
                print("[!] Uso: new <nombre_archivo>")

        elif cmd == "list":
            ide.archivos.listar()

        elif cmd == "switch":
            if args:
                ide.archivos.cambiar_activo(args[0])
            else:
                print("[!] Uso: switch <id_o_nombre>")

        elif cmd == "delete":
            if args:
                ide.archivos.eliminar(args[0])
            else:
                print("[!] Uso: delete <id_o_nombre>")

        elif cmd == "config":
            if args:
                ide.cargar_configuracion(args[0])
            else:
                print("[!] Uso: config <ruta_archivo_json>")

        elif cmd == "check":
            ide.verificar_sintaxis()

        elif cmd == "undo":
            ide.deshacer()

        elif cmd == "redo":
            ide.rehacer()

        elif cmd == "edit":
            if args:
                ide.editar_contenido(" ".join(args))
            else:
                print("[!] Uso: edit <nuevo_contenido>")

        elif cmd == "sort":
            if len(args) >= 2:
                ide.ordenar_diagnosticos(args[0], args[1])
            else:
                print("[!] Uso: sort <criterio: line|gravedad> <algoritmo: mergesort>")

        elif cmd == "analyze":
            ide.solicitar_analisis_ia()

        elif cmd == "queue-status":
            ide.estado_cola()

        elif cmd == "help":
            print("\nComandos CLI disponibles:")
            print("  new <nombre>                  - Crea un archivo en memoria")
            print("  list                          - Lista los archivos abiertos")
            print("  switch <id/nombre>            - Cambia el archivo activo")
            print("  delete <id/nombre>            - Cierra y elimina un archivo")
            print("  config <ruta.json>            - Carga el archivo de configuracion")
            print("  check                         - Valida balanceo de agrupacion")
            print("  edit <texto>                  - Modifica el codigo del archivo activo")
            print("  undo / redo                   - Deshace / Rehace cambios")
            print("  sort <criterio> <algoritmo>   - Ordena los diagnósticos")
            print("  analyze                       - Encola analisis en buffer IA")
            print("  queue-status                  - Muestra la cola de peticiones")
            print("  exit                          - Salir del programa")

        elif cmd == "exit":
            print("Cerrando Synthetix Studio...")
            break
        else:
            print(f"[!] Comando '{cmd}' desconocido. Escribe 'help' para ver opciones.")

if __name__ == "__main__":
    ejecutar_cli()