"""Punto de entrada principal de la aplicación CLI."""

import csv

# Lista en memoria para almacenar tareas durante la ejecución.
todos = []


def add_one_task(title):
    """Añade una tarea a la lista en memoria."""
    todos.append(title)


def print_list():
    """Muestra todas las tareas pendientes con numeración desde 1."""
    if not todos:
        print("No hay tareas pendientes.")
        return

    for position, task in enumerate(todos, start=1):
        print(f"{position}. {task}")


def delete_task(number_to_delete):
    """Elimina una tarea según la posición mostrada al usuario."""
    if number_to_delete < 1 or number_to_delete > len(todos):
        print("La posición no es válida.")
        return

    index_to_delete = number_to_delete - 1
    del todos[index_to_delete]


def save_todos():
    """Guarda el estado actual de la lista de tareas en todos.csv."""
    with open("todos.csv", mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for task in todos:
            writer.writerow([task])


def load_todos():
    """Carga las tareas desde todos.csv y reconstruye la lista en memoria."""
    todos.clear()

    try:
        with open("todos.csv", mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row:
                    todos.append(row[0])
    except FileNotFoundError:
        return


def main():
    """Ejecuta el menú principal de la CLI de tareas."""
    while True:
        print("\n--- MENU TODO LIST CLI ---")
        print("1. Agregar una nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Eliminar una tarea")
        print("4. Guardar tareas en todos.csv")
        print("5. Cargar tareas desde todos.csv")
        print("6. Salir")

        option = input("Selecciona una opcion (1-6): ").strip()

        if option == "1":
            title = input("Escribe el titulo de la tarea: ").strip()
            add_one_task(title)
            print("Accion ejecutada: tarea agregada.")

        elif option == "2":
            print("Accion ejecutada: mostrar tareas.")
            print_list()

        elif option == "3":
            number_text = input("Escribe el numero de la tarea a eliminar: ").strip()
            try:
                number_to_delete = int(number_text)
            except ValueError:
                print("La entrada no es valida. Debes escribir un numero entero.")
                continue

            previous_count = len(todos)
            delete_task(number_to_delete)
            if len(todos) < previous_count:
                print("Accion ejecutada: tarea eliminada.")
            else:
                print("Accion ejecutada: no se elimino ninguna tarea.")

        elif option == "4":
            save_todos()
            print("Accion ejecutada: tareas guardadas en todos.csv.")

        elif option == "5":
            load_todos()
            print("Accion ejecutada: tareas cargadas desde todos.csv.")

        elif option == "6":
            print("Saliendo de la aplicacion...")
            break

        else:
            print("La opcion no es valida. Elige un numero del 1 al 6.")


if __name__ == "__main__":
    main()
