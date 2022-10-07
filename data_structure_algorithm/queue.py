# Queue
"""
# FIFO (First in First out)
# Enqueue - add an item to the end of the line
# Dequeue - remove an item from the front of the line
# Queues are good for modeling anything you wait in line for
# e.g. Bank tellers. Placing an order at Mcdonalds
# DMV customer service. Supermarket checkout
"""

# Queue using Python Deque
from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())


class Queue():
    def __init__(self, items = None):
        if items == None:
            self.queue = deque()
        else:
            self.queue = deque(items)
    def enque(self, item):
        self.queue.append(item)
    def enque_head(self, item):
        self.queue.appendleft(item)
    def deque(self):
        if self.queue.count > 0:
            return self.queue.pop()
        else:
            return None
    def deque_head(self):
        if self.queue.count > 0:
            return self.queue.popleft()
        else:
            return None
    def enque_items(self, items=None):
        if items == None:
            return
        else: 
            self.queue.extend(items)
    def enque_items_head(self, items=None):
        if items == None:
            return
        else: 
            self.queue.extendleft(items)
    def __str__(self):
        return str(self.queue)


queue = Queue([1, 2, 3, 4])
queue.enque(5)
queue.enque_head(0)
print(queue)

