completed_count = 1
plan_count = 1

def print_file():
    with open('planned_task.csv', "r") as file:
        print(file.read())
    

def writer_completed(list):
    global completed_count
    with open('planned_task.csv', 'a') as file:
        file.write(f'Завершенная задача №{completed_count}: ')
        for e in list:
            file.write(f'{e} ')
        file.write('\n')    
    completed_count +=1        
    

def writer_planned(list):
    global plan_count
    with open('planned_task.csv', 'a') as file:
        file.write(f'Планируемая задача №{plan_count}: ')
        for e in list:
            file.write(f'{e} ')
        file.write('\n')    
    plan_count +=1     

a = ('25.07', 'Завтрак', 'мюсли')
b = ('26.07', 'Встреча', 'По работе')

writer_completed(a)
writer_completed(b)

writer_planned(a)
writer_planned(b)
    