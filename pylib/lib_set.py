
# A simple set ADT implementation. It uses the builtin set() python type and extends it.
class Set:
    def __init__(self):
        self.set: set = set()
    
    def __len__(self):
        return len(self.set)
    
    def __iadd__(self, element: any):
        self.add(element)
        return self

    def is_empty(self):
        if len(self.set) <= 0:
            return True
        
        return False

    def add(self, value: any):
        self.set.add(value)
    
    def remove(self, value: any):
        try:
            self.set.remove(value)
        except KeyError:
            print("WARN: Cannot remove a value that isn't in the set!")
    
    def contains(self, value: any):
        if value in self.set:
            return True
        
        return False