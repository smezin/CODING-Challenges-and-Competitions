class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self, order):
        print(order)
        if self.root is not None:
            if order == 'in':
                self.in_order_printTree(self.root)
            elif order == "post":
                self.post_order_printTree(self.root) 
            elif order == 'pre':
                self.pre_order_printTree(self.root) 
            else:
                return 

    def visit(self, node):
        print(str(node.v))

    def in_order_printTree(self, node):
        if node is not None:
            self.in_order_printTree(node.l)
            self.visit(node)
            self.in_order_printTree(node.r)

    def post_order_printTree(self, node):
        if node is not None:
            self.post_order_printTree(node.l)
            self.post_order_printTree(node.r)
            self.visit(node)

    def pre_order_printTree(self, node):
        if node is not None:
            self.visit(node)
            self.pre_order_printTree(node.l)
            self.pre_order_printTree(node.r)

def tree_builder(tree, values):
    for v in values:
        tree.add(v)
#     3
# 0     4
#   2      8
tree = Tree()
tree_builder(tree, [30,20,50,70,60,10,25,80])

#tree.printTree('pre')
#tree.printTree('in')
tree.printTree('post')
