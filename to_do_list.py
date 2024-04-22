# TASK LIST MANAGER: 


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
        if task_id in self.task_list.keys():
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
    num = input('What would you like to do? (provide the number)')
    ok_response = ['1', '2', '3', '4', '5']
    # change while loop to simpler statement and add num = input inside loop? 
    while num in ok_response:
        if num == '5':
            print('You are exiting the task manager. Have a nice day!')
            break
        elif num == '1':
            task_id += 1
            description = input('Enter the task description: ')  
            newTask = Task(task_id, description)
            all_tasks.add_task(newTask)
            print(f"'{newTask.description}' was added successfully.")
            num = input('What would you like to do? (provide the number)')
            if num not in ok_response:
                print('Not a valid answer, please try again.')
                num = input('What would you like to do? (provide the number)')
        elif num == '2':
            task_id = input('What is the ID of the task you\'d like to remove?')
            all_tasks.remove_task(task_id) # doesn't remove - DEBUG
            print(f"'{newTask.description}' was removed successfully.")
            num = input('What would you like to do? (provide the number)')
            if num not in ok_response:
                print('Not a valid answer, please try again.')
                num = input('What would you like to do? (provide the number)')
        elif num == '3':
            task_id = input('What is the ID of the task you\'d like to complete?')
            if task_id == newTask.task_id:
                newTask.complete_task()
            print(f"'{newTask.description}' was completed!")
            num = input('What would you like to do? (provide the number)')
            if num not in ok_response:
                print('Not a valid answer, please try again.')
                num = input('What would you like to do? (provide the number)')
        elif num == '4':
            print(all_tasks.task_list)
            num = input('What would you like to do? (provide the number)')
            if num not in ok_response:
                print('Not a valid answer, please try again.')
                num = input('What would you like to do? (provide the number)')
        else:
            print('Not a valid answer, please try again.')
            num = input('What would you like to do? (provide the number)')

main()

# edit the formatting of the tasks 