# Write your solution here:
class Task:
    total_tasks = 0
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        Task.total_tasks += 1
        self.id = Task.total_tasks
        self.__finished = False

    def is_finished(self):
        return self.__finished

    def finished_status(self):
        finished = 'NOT FINISHED'
        if self.__finished:
            finished = 'FINISHED'
        return finished

    def mark_finished(self):
        self.__finished = True

    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished_status()}'

class OrderBook:
    def __init__(self):
        self.__tasks = []
    
    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.__tasks.append(task)

    def all_orders(self):
        return self.__tasks
    
    def programmers(self):
        return list(set([task.programmer for task in self.__tasks]))

    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f'Order with {id} does not exist')

    def finished_orders(self):
        return [task for task in self.__tasks if task.is_finished() == True]

    def unfinished_orders(self):
        return [task for task in self.__tasks if task.is_finished() == False]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f'No such {programmer} exists')
        tasks = [task for task in self.__tasks if task.programmer == programmer]
        finished = 0
        unfinished = 0
        finished_workload = 0
        unfinished_workload = 0
        for task in tasks:
            if task.is_finished():
                finished += 1
                finished_workload += task.workload
            else:
                unfinished += 1
                unfinished_workload += task.workload
        return (finished, unfinished, finished_workload, unfinished_workload)
    

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)