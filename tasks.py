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
    print("Tarea agregada")


def list_tasks(tasks):
    if not tasks:
        print("No hay tareas")
        return

    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        print(f'{task["id"]}. {task["title"]} [{status}]')


def complete_task(tasks, task_id):
    # TODO: Implementar
    pass


def delete_task(tasks, task_id):
    # TODO: Implementar
    pass
