
from process_file import print_file
from process_data import build_compl
from process_data import build_planned


def project():
    work = True
    while work:
        try:
            task = request()
            if task == 1 or 2 or 3 or 4:
                if task == 4:
                    work = False
                elif task == 1:
                    var_choice = plann_or_compl()
                    if var_choice == "w":
                        user_input = str(input("Введите задачу в формате (Дата задача примечание): "))
                        print(build_planned(user_input))
                        print("Запись добавдена!")
                        project()
                    elif var_choice == "c":
                        user_input = str(input("Введите задачу которую выполнили: "))
                        build_compl(user_input)
                        print("Задача выполнена!")
                        project()
                    elif var_choice == "d":
                        user_input = str(input("Введите задачу которую удаляем: "))

                elif task == 2:
                    print_file()
                    project()

                elif task == 3:
                    project()
                
                elif task < 1 or task > 4:
                    print("Введен не правельный запрос!")
                    project()
        except ValueError:
            print("Введен не правельный запрос!")             
    else:
        print("Всего доброго!")
def request():
    print("Планируем дела")
    user_request = int(input("Добавить новую задачу - 1 Просмотр текущих дел - 2  Просмотр завершенных дел -3 Выход - 4 :"))

    return user_request

def plann_or_compl():
    user_choice = str(input("Редактировать задачу - w Отметить задачу выполненной - c Удалить задачу - d" ))
    return user_choice

