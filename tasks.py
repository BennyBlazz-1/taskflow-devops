def add_task(tasks, title):
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
    # TODO: Implementar
    pass
