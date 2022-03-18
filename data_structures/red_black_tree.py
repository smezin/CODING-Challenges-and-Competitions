from typing import List

class RBNode:
    """
    Node optimized to maintain robust and clear red-black tree.
    For keeping current and further featutres consice and fluent, 
    node comes with several utility methods to check siblings status
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.is_black = False
        self.parent = None
        self.right = None
        self.left = None

    def __str__(self) -> str:
        return str(self.value)
    
    def _is_parent_left_child(self) -> bool:
        return self.parent.left is self
    
    def _is_parent_right_child(self) -> bool:
        return not self._is_parent_left_child()

    def _is_uncle_black(self) -> None:
        if not self.parent or not self.parent.parent: 
            return None
        if self.parent._is_parent_left_child():
            uncle = self.parent.parent.right
        else:
            uncle = self.parent.parent.left
        return uncle.is_black

class RBTree:
    """
    Red_Black tree implementation. Incliding insert, search, delete.
    RBTree class relies on RBNode, but for some reasons decided to not 
    contain RBNode as sub class, although you can do that/
    """
    def __init__(self) -> None:
        self.root = None
   
    def insert_one(self, value: int) -> None:
        if self.root is None:
            self.root = RBNode(value)
        else:
            self._insert_one(self.root, value)
        return 

    def insert_many(self, values: List[int]) -> None:
        for value in values:
            self.insert_one(value)

    def search(self, value: int, subtree_root: RBNode = None) -> RBNode:
        if subtree_root is None:
            subtree_root = self.root
        return self._search(value, subtree_root)

    def in_order_travers(self) -> List[int]:
        if self.root is None:
            return None
        node_values = []
        self._in_order_travers(self.root, node_values)
        return node_values
    
    def delete(self, value: int, subtree_root: RBNode = None) -> None:
        if subtree_root is None:
            subtree_root = self.root
        node = self.search(value, subtree_root)
        #sanity check
        if node is None:
            return
        if subtree_root is None:
            subtree_root = self.root
        #case 1: no children
        if node.right is None and node.left is None:
            if node is self.root:
                self.root = None
            if node._is_parent_left_child():
                node.parent.left = None         #gc will clean it up
            elif node._is_parent_right_child():
                node.parent.right = None
        #case 2: single child
        if node.right is None and node.left is not None:
            node = node.left
        elif node.left is None and node.right is not None:
            node = node.right
        #case 3: two children
        if node.left is not None and node.right is not None:
            min_value_node = self._min_child(node.right.value)
            node.value = min_value_node.value
            self.delete(min_value_node.value, node.right)
        
    def _min_child(self, value: int) -> RBNode:
        node = self.search(value)
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node

    def _in_order_travers(self, node: RBNode, node_values: List[int]) -> None:
        if node:
            self._in_order_travers(node.left, node_values)
            node_values.append(node.value)
            self._print_data(node.value, node.parent, node.left, node.right)
            self._in_order_travers(node.right, node_values)
    
    def _rotate_left(self, value: int) -> None: 
        pivot = self.search(value)
        if pivot is None:
            return
        new_top = pivot.right
        pivot.right = new_top.left
        if new_top.left:
            new_top.left.parent = pivot
        new_top.parent = pivot.parent
        if pivot.parent is None:
            self.root = new_top
        elif pivot._is_parent_left_child():
            pivot.parent.left = new_top
        else:
            pivot.parent.right = new_top
        new_top.left = pivot
        pivot.parent = new_top

    def _rotate_right(self, value: int) -> None: 
        """
        param value: indicates the value of the node to rotate around
        """
        pivot = self.search(value)              #rotating around the pivot (current subtree top)
        if pivot is None:
            return
        new_top = pivot.left                    #rotating right, hence the new top is the old top left child
        pivot.left = new_top.right              #fixing edge 1
        if new_top.right:                       
            new_top.right.parent = pivot
        new_top.parent = pivot.parent
        if pivot.parent is None:
            self.root = new_top
        elif pivot._is_parent_right_child():     #if pivot is it's parent right child
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
        if node is None or value is None: 
            return 
        elif node.value == value:
            return node
        elif value > node.value:
            return self._search(value, node.right)
        else:
            return self._search(value, node.left)
    
    def _print_data(self, v, p, l, r):
        print(f'value: {v} \tparent: {p} \tleft: {l} \tright: {r}')
        


rb = RBTree()
rb.insert_many([4,2,6,1,3,5,7])
#rb.insert_many([6,4,7,2,5,1,3])

#print(rb.search(4))
print(rb.in_order_travers())
#rb._rotate_left(4)
#print(rb._min_child(4))
#rb._rotate_right(6)
rb.delete(4)
print(rb.in_order_travers())


    