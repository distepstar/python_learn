# MaxHeap
"""
# Complete binary tree
# Every node <= its parent
"""

"""
MaxHeap is FAST!
# Insert in O(log n)
# Get Max in O(1)
# Remove Max in O(log n)
"""

# Easy to implement using a List
"""
# i = 4
# parent(i) = i/2 = 2
# left(i) = i * 2 = 8
# right(i) = i * 2 + 1 = 9
"""

# MaxHeap Operaitons
"""
# Push(insert)  - add value to end of array
                - float it up to its proper position
                - (12 > 11 ?)
                - (12 > 16 ?)
# Peek(get max) - return the value at heap[1]
# Pop(remove Max)   - move max to end of array
                    - delete it
                    - bubble down the item at index 1 to its proper position
                    - return max
"""


# Python MaxHeap
from re import A


class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__float_up(len(self.heap) - 1)
    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max
    
    def __swap(self, i , j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        # // is to round down -> get integer
        parent = index//2
        # hits the top
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            # recursion to check if the parent is larger than its parent
            self.__float_up(parent)

    def __bubble_down(self, index):
        # get sub-item on left
        left = index * 2
        # get sub-item on right
        right = (index * 2) + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            # recursion call to swap down the item
            self.__bubble_down(largest)
    
    def __str__(self):
        return str(self.heap)

m = MaxHeap([95, 3, 21])
m.push(10)

print(m)
print(m.pop())
print(m.peek())


