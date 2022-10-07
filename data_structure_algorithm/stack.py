# Stack
"""
# LIFO (Last in First out))
# Push - place item onto the stack
# Pop - took item off of the stack
# Peek - get item on top of stack, without removing it
# Clear - clear all the items from the stack
# Undo - track which commands have been executed. Pop last command off command stack to undo it
"""

# Stack using Python List
my_stack = list()
# push
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(9)
print(my_stack)


print(my_stack.pop())
print(my_stack.pop())
print(my_stack)

# Stack using List with a Wrapper Class
"""
We create a Stack class and a full set of Stack methods
But the underlying data structure is really a Python List
For pop and peek methods we first check whether the stack is empty, to avoid exceptions
"""

# Custom stack class
class Stack():
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    def __str__(self):
        return str(self.stack)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(4)
my_stack.push(8)
my_stack.push(16)

print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())




