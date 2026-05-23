
class Stack:

    def __init__(self):
        self.items = []
    
    def push(self,value): 
        self.items.append(value)

    def push_all(self, values):
        for i in values:
            self.push(i)

    def pop(self):
        popped_item = self.get_peek(); 
        self.items.pop()
        return popped_item

    def get_peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return self.get_stack_size() == 0

    def get_stack_size(self):
        return len(self.items) 

    def get_current_stack(self):
        return self.items  

    def clear_stack(self):
        for i in range(self.get_stack_size()):
            self.pop() 