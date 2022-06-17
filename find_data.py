#planned_task.csv
#completed_task.csv

def find_plans(filename, key_word):

    find_plans = open(filename, mode='r+')

    find_plans = find_plans.readlines()

    for line in find_plans:

        if key_word.lower() in line.lower():

            print(line)

start = int(input("Привет! Какой блокнот тебе открыть? Если 'Планы', то введи цифру 1, если 'Завершенные дела', то введи цифру 2 =>"))

if start == 1:
    key_word = input("Введи ключевое слово для поиска задачи => ")
    find_plans('planned_task.csv', key_word)
elif start ==2:
    key_word = input("Введи ключевое слово для поиска задачи => ")
    find_plans('completed_task.csv', key_word)
else:
    print("Товарищ, такого блокнота у тебя нет! Только 1 или 2.")

