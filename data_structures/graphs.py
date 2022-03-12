from typing import Tuple

class Node:
    def __init__(self, value: Tuple[int, int]):
        self.value = value
        self.next = None
    
class DirectedGraph:
    def __init__(self, node):
        self.root = node
    
    
