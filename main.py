tack = []
while True:
    x = int(input("1. Показать список\n"
                  "2. Добавить задачу\n"
                  "3. Удалить задачу\n"
                  "4. Выход \n"
                  "Введите действие:\n"))
    match x:
        case 1:
            if not tack:
                print("Список пуст")
            else:
                print(tack)
            continue


        case 2:
            x = input("Введите задачу которую нужно добавить:")
            tack.append(x)
            print(f"Успешно добавили задачу {x}")

        case 3:
            print(tack)
            y = int(input("Введите номер задачи которую нужно удалить:"))
            tack.pop(y-1)
            if not tack:
                print("Список пуст")
            else:
                print(tack)

        case 4:

            break

