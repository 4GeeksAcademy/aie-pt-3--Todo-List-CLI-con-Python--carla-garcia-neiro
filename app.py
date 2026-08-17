"""Punto de entrada principal de la aplicación CLI."""

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


def main():
    """Prueba básica de Fase 1 y Fase 2."""
    add_one_task("Preparar pedido")
    add_one_task("Llamar al transportista")
    add_one_task("Revisar inventario")

    print_list()


if __name__ == "__main__":
    main()
