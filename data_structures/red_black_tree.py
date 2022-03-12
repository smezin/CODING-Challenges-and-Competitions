from typing import List

class RBNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.is_black = False
        self.parent = None
        self.right = None
        self.left = None
        #self.data = None

    def __str__(self):
        return str(self.value)
    
    def is_uncle_black(self) -> None:
        if not self.parent or not self.parent.parent: 
            return None
        if self.parent is self.parent.parent.left:
            uncle = self.parent.parent.right
        else:
            uncle = self.parent.parent.left
        return uncle.is_black

    def is_parent_left_child(self) -> bool:
        """
        return indication if current node is left child of it's parent
        """
        return self.parent.left is self
    
    def is_parent_right_child(self) -> bool:
        """
        return indication if current node is left child of it's parent
        """
        return not self.is_parent_left_child()

class RBTree:
    """
    Red_Black tree implementation. Incliding insert, search, delete
    """
    def __init__(self) -> None:
        self.root = None
    
    def get_root(self) -> RBNode:
        return self.root
    
    def insert_one(self, value: int) -> None:
        if not self.root:
            self.root = RBNode(value)
        else:
            self._insert_one(self.root, value)
        return 

    def insert_many(self, values: List[int]) -> None:
        for value in values:
            self.insert_one(value)

    def search (self, value: int) -> RBNode:
        return self._search(value, self.root)

    def rotate_left(self, value: int) -> None: 
        """
        param value: indicates the value of the node to rotate around
        """
        pivot = self.search(value)
        new_top = pivot.right
        pivot.right = new_top.left
        if new_top.left:
            new_top.left.parent = pivot
        new_top.parent = pivot.parent
        if pivot.parent is None:
            self.root = new_top
        elif pivot.is_parent_left_child():
            pivot.parent.left = new_top
        else:
            pivot.parent.right = new_top
        new_top.left = pivot
        pivot.parent = new_top

    def rotate_right(self, value: int) -> None: 
        """
        param value: indicates the value of the node to rotate around
        """
        pivot = self.search(value)              #rotating around the pivot (current subtree top)
        new_top = pivot.left                    #rotating right, hence the new top is the old top left child
        pivot.left = new_top.right              #fixing edge 1
        if new_top.right:                       
            new_top.right.parent = pivot
        new_top.parent = pivot.parent
        if pivot.parent is None:
            self.root = new_top
        elif pivot.is_parent_right_child():       #if pivot is it's parent right child
            pivot.parent.right = new_top
        else:
            pivot.parent.left = new_top
        new_top.right = pivot
        pivot.parent = new_top

    def _insert_one(self, node: RBNode, value: int) -> None:
        if value >= node.value:
            if node.right:
                self._insert_one(node.right, value)
            else:
                new_node = RBNode(value)
                new_node.parent = node
                node.right = new_node
        else:
            if node.left:
                self._insert_one(node.left, value)
            else:
                new_node = RBNode(value)
                new_node.parent = node
                node.left = new_node

    def _search (self, value: int, node: RBNode) -> RBNode:
        """
        param value: value to be searched
        param node: RBNode to begin search. can be root to search whole tree or node for searching subtree
        output param: the node with the value if found, None otherwise
        """
        if not node: 
            return False
        elif node.value == value:
            return node
        elif value > node.value:
            return self._search(value, node.right)
        else:
            return self._search(value, node.left)
    
    def in_order_travers(self) -> List[int]:
        if not self.root:
            return None
        node_values = []
        self._in_order_travers(self.root, node_values)
        return node_values
    
    def _in_order_travers(self, node: RBNode, node_values):
        if node:
            self._in_order_travers(node.left, node_values)
            node_values.append(node.value)
            self.print_data(node.value, node.parent, node.left, node.right)
            self._in_order_travers(node.right, node_values)
    
    def print_data(self, v, p, l, r):
        print(f'value: {v} \tparent: {p} \tleft: {l} \tright: {r}')
        


rb = RBTree()
rb.insert_many([4,2,6,1,3,5,7])
#rb.insert_many([6,4,7,2,5,1,3])

#print(rb.search(4))
print(rb.in_order_travers())
rb.rotate_left(4)
rb.rotate_right(6)
print(rb.in_order_travers())


    