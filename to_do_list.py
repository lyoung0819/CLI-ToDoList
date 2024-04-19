# THIS IS THE RETRY: 



class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id,
        self.description = description,
        self.status = False 

    def complete_task(self):
        self.status = True

    def __str__(self):
        status = ['[X]' if self.status else '[ ]']
        return f'{self.task_id}. {self.status} {self.description} '
    
class TaskList:
    def __init__(self, name):
        self.name = name
        self.task_list = {}
    
    def add_task(self, task):
        self.task_list[task.task_id] = task.description
        return f"'{task.description}' has been added!"
    
    def remove_task(self, task_id):
        if task_id in self.task_list:
            del self.task_list[task_id]
        return 'Your task has been removed.'
    
    def show_tasks(self):
        print('MY TASKS:')
        print('----------')
        for key, val in self.task_list.items():
            return f'{key}. {val}'
        


def main():
    task_id = 0
    name = input('Enter your name: ').title()
    all_tasks = TaskList(name)
    print(f'Hello {name}! Welcome to your task manager. Below are your options:')
    print('''
    1. Add a task
    2. Remove a task
    3. Complete a task
    4. See all tasks
    5. Quit task manager
          ''')
    user_inp = input('What would you like to do? (provide the number)')
    num = int(user_inp)
    while num != 5:
        if num == 1:
            task_id += 1
            description = input('Enter the task description: ')
            newTask = Task(task_id, description)
            all_tasks.add_task(newTask)
        elif num == 2:
            task_id = input('What is the ID of the task you\'d like to remove?')
            all_tasks.remove_task(task_id)
        elif num == 3:
            pass
        elif num == 4:
            return all_tasks
        elif num == 5:
            print('You are exiting the task manager. Have a nice day!')
            break
        else:
            print('Not a valid answer, please try again.')
            user_inp = input('What would you like to do? (provide the number)')

    


main()