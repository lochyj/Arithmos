
# A simple list ADT that builds on the inbuilt python List type
class List:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def __iadd__(self, element: any):
        self.append(element)
        return self

    def is_empty(self):
        if len(self.list) <= 0:
            return True

        return False
    
    def append(self, element):
        self.list.append(element)

    def head(self):
        return self.list[0]

    def last(self):
        return self.list[-1]
    
    def remove_head(self):
        try:
            self.list.pop(0)
        except IndexError:
            print("WARN: There are no more elements in the list!")
    
    def remove_last(self):
        try:
            self.list.pop(-1)
        except IndexError:
            print("WARN: There are no more elements in the list!")