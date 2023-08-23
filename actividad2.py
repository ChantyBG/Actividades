""" Actividad 2 - Funciones: Mostrar, Agregar, Eliminar y Editar tareas """

def mostrar_tareas(tareas):
    print("Lista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")

"""Append es un método que tiene toda lista de Python el cual permite agregar un elemento al final de la lista. 
No retorna ningún elemento ni valor, además, acepta cualquier tipo de valor como elemento a agregar: 
número, cadena, lista, diccionario, objeto, etc."""

def agregar_tarea(tareas, nueva_tarea):
    tareas.append(nueva_tarea)
    print("Tarea agregada:", nueva_tarea)

"""El método len() devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario.
len() toma un argumento, que puede ser una secuencia (como una cadena, bytes, tupla, lista o rango) o colección (como un diccionario, conjunto o conjunto "set" congelado "set frozen")."""

"""list.pop([i])
Quita el ítem en la posición dada de la lista y lo retorna. Si no se especifica un índice, a.pop() quita y retorna el último elemento de la lista. 
(Los corchetes que encierran a i en la firma del método denotan que el parámetro es opcional, no que deberías escribir corchetes en esa posición. 
Verás esta notación con frecuencia en la Referencia de la Biblioteca de Python.)"""

def eliminar_tarea(tareas, indice):
    if 1 <= indice <= len(tareas):
        tarea_eliminada = tareas.pop(indice - 1)
        print("Tarea eliminada:", tarea_eliminada)
    else:
        print("Índice de tarea no válido. Revisa la lista de tareas existente.")

def editar_tarea(tareas, indice, nueva_tarea):
    if 1 <= indice <= len(tareas):
        tareas[indice - 1] = nueva_tarea
        print("Tarea editada:", nueva_tarea)
    else:
        print("Índice de tarea no válido. Revisa la lista de tareas.")

def main():
    lista_de_tareas = []

    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Agregar tarea")
        print("2. Mostrar lista de tareas")
        print("3. Eliminar tarea")
        print("4. Editar tarea")
        print("5. Salir")
        
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            nueva_tarea = input("Ingrese la nueva tarea: ")
            agregar_tarea(lista_de_tareas, nueva_tarea)
        elif opcion == "2":
            mostrar_tareas(lista_de_tareas)
        elif opcion == "3":
            indice = int(input("Ingrese el índice de la tarea a eliminar: "))
            eliminar_tarea(lista_de_tareas, indice)
        elif opcion == "4":
            indice = int(input("Ingrese el índice de la tarea a editar: "))
            nueva_tarea = input("Ingrese la nueva tarea: ")
            editar_tarea(lista_de_tareas, indice, nueva_tarea)
        elif opcion == "5":
            print("Saliendo del programa. Bye Bye")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

"""Python break es una sentencia que permite parar un bucle por completo en cuanto se da o deja de darse una condición externa. 
Python break se utiliza dentro del código y suele estar situado después de una sentencia if.
La función input() permite obtener texto escrito por teclado. 
Al llegar a la función, el programa se detiene esperando que se escriba algo y se pulse la tecla Enter"""   

if __name__ == "__main__":
    main()