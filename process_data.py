
# def build_planned(string):
#     record = string
#     final_record = tuple( i for i in record.split(' '))
#     return final_record

# def build_compl(string):
#     record = string
#     final_record = tuple( i for i in record.split(' '))
#     return final_record


'''
От пользователя получаем строку с "делом"
По ключу, пользователь определяет статус "дела" (запланированное или выполненное)
Строку преобразуем в кортеж

'''

print('Привет user')

user_input = input(
    'Введите  запись (в качестве разделителя используйте пробел): ')
key_note = int(input(
    "В какой блолкнот внести запись? Если 'Планы', то введите цифру 1, если 'Завершённые дела', то введите цифру 2 =>  "))


def creating_record(string):
    if key_note == 1:
        plan_record = tuple(i for i in string.split(' '))
        return plan_record
    elif key_note == 2:
        compl_record = tuple(i for i in string.split(' '))
        return compl_record
    else:
        print('Неверно задан номер блокнота! Введите цифру 1 Планирование дела или цифру 2 для Завершенного дела')

# print(creating_record(user_input))
