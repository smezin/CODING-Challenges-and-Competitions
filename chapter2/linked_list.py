
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def __str__(self):
        node = self.head
        i = 0
        res = ''
        while node is not None:
            res += (f'node n {i}, node v {node.data} \n')
            node = node.next
            i += 1
        return res

    def add_to_tail(self, node):
        last_node = self.head
        while last_node is not None:
            #print('ittr->',last_node.data)
            prev = last_node
            last_node = last_node.next
        #print('tail->',prev.data)
        prev.next = node   

    def find_kth_from_end(self, k):
        node = self.head
        for i in range (k):
            if node.next is None:
                return -1
            node = node.next
    
    def delete_from_middle(self, node_to_del):
        back_runner = self.head
        front_runner = self.head.next
        while front_runner.next != node_to_del:
            back_runner = back_runner.next
            front_runner = front_runner.next
        back_runner.next = front_runner.next

        front_runner = front_runner.next
        back_runner = self.head
        while front_runner is not None:
            back_runner = back_runner.next
            front_runner = front_runner.next
        return back_runner

    def partition(self, k):
        node = self.head
        left_head = self.head
        right_tail = self.head

        while node is not None:
            next = node.next
            if node.data < k:
                node.next = left_head
                left_head = node
            else:
                right_tail.next = node
                right_tail = node
            node = next
        # print(left_head)
        # print(right_tail)
        right_tail.next = None
        self.head = left_head

    def partition1(self, k):
        node = self.head
        head = self.head
        tail = self.head
        while (node is not None):
            next = node.next
            if (node.data < k):
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node
            node = next
        
        tail.next = None
        self.head = head
first = Node(0)
l = LinkedList(first)
l.add_to_tail(Node(1))
l.add_to_tail(Node(2))
l.add_to_tail(Node(3))
l.add_to_tail(Node(4))
l.add_to_tail(Node(5))
l.add_to_tail(Node(6))
l.add_to_tail(Node(7))
l.add_to_tail(Node(8))

print(l)
l.partition(5)
print(l)
#print(l.find_kth_from_end(7))

