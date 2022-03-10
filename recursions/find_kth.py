class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedListy:
    def __init__(self, node = None):
        self.head = node

    def __str__(self):
        s = []
        node = self.head
        while node is not None:
            s.append(node.value)
            node = node.next
        return str(s)

    def add(self, node, i = 0):
        if i == 0:
            node.next = self.head
            self.head = node
            return

        next_index = 1
        current_node = self.head
        while current_node is not None:
            if i == next_index:
                node.next = current_node.next
                current_node.next = node
                return
            next_index += 1
            current_node = current_node.next

    def return_kth(self, k, node = None):
        if node is None:
            node = self.head
        if node.next is None:
            return 0
        index = self.return_kth(k, node.next) + 1
        if k == index:
            print (f'{node} is {k}th to end')
        return index 



node = Node(10)
ll = LinkedListy(node)
ll.add(Node(11))
ll.add(Node(12), 1)
ll.add(Node(13))
ll.add(Node(33))
ll.add(Node(23))
print(ll)
ll.return_kth(2)



