
class PriorityQueue:
    def __init__(self):
        self.queue: list[any, int] = []

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def insert_with_priority(self, element: any, priority: int):

        for index, el in enumerate(self.queue):
            if el[1] <= priority:
                self.queue.insert(index, (element, priority))
                return

        self.queue.append((element, priority))

    def remove_min(self):
        try:
            return self.queue.pop()[0]
        except IndexError:
            print("WARN: Cannot serve / dequeue an empty queue!")
            return None

    def get_min(self):
        try:
            return self.queue[0][0]
        except IndexError:
            print("WARN: Cannot peek an empty queue!")
            return None