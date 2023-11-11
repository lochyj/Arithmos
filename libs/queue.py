
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def append(self, element):
        self.queue.append(element)

    def enqueue(self, element):
        self.append(element)

    def serve(self):
        try:
            return self.queue.pop()
        except IndexError:
            print("WARN: Cannot serve / dequeue an empty queue!")
            return None

    def dequeue(self):
        return self.serve()

    def peek(self):
        try:
            return self.queue[0]
        except IndexError:
            print("WARN: Cannot peek an empty queue!")
            return None