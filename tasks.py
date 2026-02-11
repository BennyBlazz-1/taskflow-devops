def add_task(tasks, title):
    # Verificar si ya existe una tarea con el mismo título
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("Error: ya existe una tarea con ese título")
            return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("✅ Tarea agregada")


def list_tasks(tasks):
    if not tasks:
        print("No hay tareas")
        return

    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        print(f'{task["id"]}. {task["title"]} [{status}]')


#  FUNCIÓN DE VALIDACIÓN DE ID
def validar_task_id(task_id):
    """
    Valida que el task_id:
    - Sea un número
    - No sea negativo
    - No rompa el programa si es inválido
    """
    try:
        task_id = int(task_id)
    except ValueError:
        print("❌ Error: El ID debe ser un número (no letras ni símbolos).")
        return None

    if task_id < 0:
        print("❌ Error: El ID no puede ser negativo.")
        return None

    return task_id


def complete_task(tasks, task_id):
<<<<<<< HEAD
    task_id = validar_task_id(task_id)
    if task_id is None:
        return  # 🔁 No se rompe el menú

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("✅ Tarea marcada como completada")
            return

    print("❌ Error: No se encontró una tarea con ese ID")


def delete_task(tasks, task_id):
    task_id = validar_task_id(task_id)
    if task_id is None:
        return  # 🔁 No se rompe el menú
=======
    try:
        task_id = int(task_id)
    except:
        print("Error: ID inválido")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("La tarea ya estaba completada")
                return
            task["completed"] = True
            print("✔ Tarea completada")
            return

    print("Error: tarea no encontrada")



def delete_task(tasks, task_id):
    try:
        task_id = int(task_id)
    except:
        print("Error: ID inválido")
        return

    for task in tasks:
        if task["id"] == task_id:
            confirm = input(f"¿Seguro que deseas eliminar '{task['title']}'? (s/n): ")

            if confirm.lower() != "s":
                print("Eliminación cancelada")
                return
            tasks.remove(task)

            for i, t in enumerate(tasks):
                t["id"] = i + 1

            print("Tarea eliminada")
            return

    print("Error: ID no encontrado")

    print("Error: ID no encontrado")
>>>>>>> upstream/main
