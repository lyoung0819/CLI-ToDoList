# TASK LIST MANAGER: 


class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id,
        self.description = description 
        self.status = False

    def complete_task(self):
        self.status = True
    
class TaskList:
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task_id, task):
        new_task = Task(task_id, task)
        self.task_list.append([new_task.task_id, new_task.description, new_task.status])
        print("Your task has been added!")
    
    def remove_task(self, task_id):
        for lst in self.task_list:
            if lst[0] == task_id:
                self.task_list.pop(lst)
                print('Your task has been removed.')
        else:
            print('No task with that ID was found.')
    
    def show_tasks(self):
        print('MY TASKS:')
        for lst in self.task_list:
            print(f"{lst[0]}. {lst[1]} | completed: {lst[2]}")

    def complete_task(self, task_id):
        for lst in self.task_list:
            if task_id == lst[0]:
                lst[2] == True
                print('Your task has been completed.')
            else:
                print('Could not find task with that ID')

        


def main():
    task_id = 0
    name = input('Enter your name: ').title()
    my_tasks = TaskList()
    print(f'Hello {name}! Welcome to your task manager. Below are your options:')
    print('''
    1. Add a task
    2. Remove a task
    3. Complete a task
    4. See all tasks
    5. Quit task manager
          ''')
    while True:
        num = input('What would you like to do? (provide the number)')
        if num == '5':
            print('You are exiting the task manager. Have a nice day!')
            return False
        elif num == '1':
            task_id += 1
            description = input('Enter the task description: ')  
            my_tasks.add_task(task_id, description)
        elif num == '2':
            task_id = input('What is the ID of the task you\'d like to remove?') 
            my_tasks.remove_task(task_id)
        elif num == '3':
            task_id = input('What is the ID of the task you\'d like to complete?')
            my_tasks.complete_task(task_id)
        elif num == '4':
            my_tasks.show_tasks()
        else:
            print('Not a valid answer, please try again.')
            continue

main()

