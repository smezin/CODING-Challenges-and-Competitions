import sys
INF = sys.maxsize

class MaxHeap:
    """
    class represents max heap.
    """
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)
    
    def get_parent(self, i):
        if i <= 0:
            return -1
        return self.heap[(i-1)//2]
    
    def get_parent_index(self, i):
        if i == 0:
            return -1
        return (i-1)//2

    def index_of_bigger_child(self, i):
        if self.get_left_child(i) > self.get_right_child(i):
            return self.get_left_child_index(i)
        return self.get_right_child_index(i)
    
    def index_of_smaller_child(self, i):
        if self.get_left_child(i) < self.get_right_child(i):
            return self.get_left_child_index(i)
        return self.get_right_child_index(i)

    def get_left_child(self, i):
        if i*2+1 > len(self.heap) - 1:
            return -INF
        return self.heap[self.get_left_child_index(i)]

    def get_left_child_index(self, i):
        if i*2+1 > len(self.heap) - 1:
            return -1
        return i*2+1

    def get_right_child(self, i):
        if i*2+2 > len(self.heap) - 1:
            return -INF
        return self.heap[self.get_right_child_index(i)]

    def get_right_child_index(self, i):
        if i*2+2 > len(self.heap) - 1:
            return -1
        return i*2+2
    
    def swap(self, i, j):
        if i >= len(self.heap) or j >= len(self.heap):
            return False
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]  
        return True

    def insert(self, item):
        self.heap.append(item)
        self.bubble_up_last()
    
    def insert_many(self, items):
        for item in items:
            self.insert(item)
    
    def insert_and_heapify(self, items):
        self.heap = items[:]
        self.heapify()
    
    def pop_max(self):
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return max_val

    def delete(self, i):
        self.heap[i] = INF
        self.bubble_up(i)
        self.pop_max()

    def heapify (self):
        last_parent_i = self.get_parent_index(len(self.heap)-1)
        for i in range(last_parent_i, -1, -1):
            self.bubble_down(i)
        
    def bubble_up_last(self):
        self.bubble_up(len(self.heap)-1)

    def bubble_up(self, i):
        if i == 0 or self.heap[i] <= self.get_parent(i):
            return
        if self.heap[i] > self.get_parent(i):
            self.swap(i, self.get_parent_index(i))
            self.bubble_up(self.get_parent_index(i))

    def bubble_down(self, i):
        if i >= len(self.heap) - 1:
            return
        
        bigger_child_i = self.index_of_bigger_child(i)
        smaller_child_i = self.index_of_smaller_child(i)
        if self.heap[i] < self.heap[bigger_child_i]:
            self.swap(i, bigger_child_i)
        elif self.heap[i] < self.heap[smaller_child_i]:
            self.swap(i, smaller_child_i) 
        else:
            return
        

h = MaxHeap()
h1 = MaxHeap()
ITEMS = [10, 15, 30, 40, 70, 100]
h.insert_and_heapify(ITEMS)
h1.insert_many(ITEMS)
print(h)
print(h1)
# h.pop_max()
# print(h)
# h.insert(50)
# print(h)
# h.insert(60)
# print(h)
# h.delete(3)
# print(h)

