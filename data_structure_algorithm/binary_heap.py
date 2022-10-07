# Binary Heap

from heapq import heappush, heappop, heapify


class MinHeap:
    def __init__(self, items=[]):
        self.heap = []
        for item in items:
            self.heap.append(item)
            self.heapify_up(len(self.heap) - 1)

    def __out_bound_except(self):
        # smaller than 1
        if len(self.heap) == 0:
            raise IndexError("Index out of bound")

    def peek(self):
        self.__out_bound_except()
        return self.heap[0]

    def pop(self):
        self.heap.pop()

    def insert(self, item):
        if len(self.heap) > 0:
            self.heap.append(item)
            self.heapify_up(len(self.heap) - 1)
        else:
            self.heap.append(item)

    def delete(self, item):
        try:
            index = self.heap.index(item)
        except ValueError:
            print(f"Item {item} does not exist in heap")

        if index == len(self.heap) - 1:
            self.heap.pop()
        else:
            # swap head tail
            self.__swap(index, len(self.heap) - 1)
            self.pop()
            print(self.heap)
            self.heapify_down(index)
        
        
    # converting list to heap
    def heapify_up(self, index):
        self.__out_bound_except()
        # get parent index -> // floor
        parent = index // 2
        # parent node
        if index <= 1:
            return 
        elif self.heap[parent] > self.heap[index]:
            self.__swap(parent, index)
            # recursion call
            self.heapify_up(parent)
    
    def heapify_down(self, index):
        # get left right index
        largest = index
        left = index*2 + 1
        right = index*2 + 2

        if len(self.heap) > left and self.heap[left] < self.heap[index]:
            largest = left
        if len(self.heap) > right and self.heap[right] < self.heap[largest]:
            largest = right
        
        if largest != index:
            self.__swap(index, largest)
            print(f"heapify_down: {self.heap}")
            self.heapify_down(largest)

    def __swap(self, t1, t2):
        self.heap[t1], self.heap[t2] = self.heap[t2], self.heap[t1]

    def __str__(self) -> str:
        return str(self.heap)


min_heap = MinHeap([1, 4, 6, 32, 12, 23])
h = [5, 1, 3, 2, 4, 9]
h2 = [1, 4, 32, 12, 23]

heapify(h)
heapify(h2)
min_heap.insert(8)
print(f"Min_heap: {min_heap}")
min_heap.delete(6)
print(f"Min_heap: {min_heap}")
print(f"h1: {h}")
print(f"h2: {h2}")