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


def main():
    """Prueba básica de Fases 1, 2 y 3."""
    add_one_task("Preparar pedido")
    add_one_task("Llamar al transportista")
    add_one_task("Revisar inventario")

    print("Lista inicial:")
    print_list()

    delete_task(2)
    print("\nLista tras delete_task(2):")
    print_list()


if __name__ == "__main__":
    main()
