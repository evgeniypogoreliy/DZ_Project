

def writer_completed(list):
    file = open('Completed_task.csv' 'w')
    file.write(str(list))
    file.close()

def writer_planned(list):
    file = open('planned_task.csv' 'w')
    file.write(str(list))
    file.close()



    