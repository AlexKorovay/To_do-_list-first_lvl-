
tasks = []
def show_tasks(tasks):
    if not tasks:
        print("Список пуст")
    else:
        print(tasks)

def tasks_append(tasks):
    x = input("Введите задачу которую нужно добавить:")
    tasks.append(x)
    print(f"Успешно добавили задачу {x}")

def tasks_pop(tasks):
    print(tasks)
    y = int(input("Введите номер задачи которую нужно удалить:"))
    tasks.pop(y - 1)
    if not tasks:
        print("Список пуст")
    else:
        print(tasks)

while True:
    x = int(input("1. Показать список\n"
                  "2. Добавить задачу\n"
                  "3. Удалить задачу\n"
                  "4. Выход \n"
                  "Введите действие:\n"))
    match x:
        case 1:
            show_tasks(tasks)
        case 2:
            tasks_append(tasks)
        case 3:
            tasks_pop(tasks)
        case 4:
            break


