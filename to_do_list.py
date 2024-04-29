# TASK LIST MANAGER: 


class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id, # going in as a tuple here? 
        self.description = description 
        self.status = False

    def complete_task(self):
        self.status = True

    def __str__(self):
        return f"Task #{self.task_id}: {self.description}, {self.status}"

    
class TaskList:
    def __init__(self):
        self.task_list = [] # list of task objects
    
    # def __str__(self):
    #     return 
    
    def add_task(self, task_id, task):
        new_task = Task(task_id, task)
        self.task_list.append([new_task.task_id, new_task.description, new_task.status]) #new_task.task_id, new_task.description, new_task.status
        print("Your task has been added!")
    
    def remove_task(self, task):
        print(self.task_list)
        for arr in self.task_list:
            if arr[1] == str(task): 
                self.task_list.remove(arr)
                print('Your task has been removed.')
            else:
                print('No task with that description was found.')
    
    def show_tasks(self):
        print('MY TASKS:')
        for lst in self.task_list:
            print(lst) # f"{lst[0]}. {lst[1]} | completed: {lst[2]}"

    def complete_task(self, task):
        for obj in self.task_list:
            if obj[1] == str(task):
                obj[2] = True
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
            task = input('What is the description of the task you\'d like to remove? (enter description)') 
            my_tasks.remove_task(task)
        elif num == '3':
            task = input('What task would you like to complete? (enter description)')
            my_tasks.complete_task(task)
        elif num == '4':
            my_tasks.show_tasks()
        else:
            print('Not a valid answer, please try again.')
            continue

main()

