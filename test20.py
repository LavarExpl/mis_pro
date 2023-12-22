user = 'test'
class Task:
    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date
        self.complete_data = False

    def completed(self):
        self.complete_data = True


class to_do():
    def __init__(self):
        self.task =[]

    def add(self):
        self.task.append(self.task)
        print('This item has been added to the list of things to do')

    def delete(self):
        print('removed')
        print(f'{user}:After you {task1.task_name} by {task1.due_date}. It will be removed from List')
 #if task in self.task:
        #    self.task.remove(task)

    def view(self):
        print('viewing list')
        print(f'{user}:{task1.task_name} and it needs to be completed by {task1.due_date}.')
 # for task in self.task:

task1 = Task('Buy food', 'monday')
task2 = Task(task_name='Garbage', due_date='friday')



t1 =to_do.add('dishes')

