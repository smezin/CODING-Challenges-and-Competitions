#Implementaion of hash table
TABLE_SIZE = 10

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        res = f'key: {self.key} value: {self.value} next: {self.next.key if self.next is not None else "--"} \n'
        node = self.next
        while node is not None:
            res += f'key: {node.key} value: {node.value} next: {node.next.key if node.next is not None else "--"} \n'
            node = node.next
        return res

class HashTable:
    def __init__(self):
        self.capacity = TABLE_SIZE
        self.buckets = [None] * TABLE_SIZE
        self.size = 0
    
    def hash (self, key):
        hash_sum = 0
        for index, c in enumerate(key):
            hash_sum += (index + len(key)) ** ord(c)
        return hash_sum % self.capacity

    def last_node(self, hashed_key):
        node = self.buckets[hashed_key]
        if (node is None):
            return 
        while node.next is not None:
            node = node.next
        return node
    
    def insert (self, key, value):
        hashed_key = self.hash(key)
        last = self.last_node(hashed_key)
        if last is None:
            self.buckets[hashed_key] = Node(key, value)
        else:
            last.next = Node(key, value)
        self.size += 1
    
    def get(self, key):
        hashed_key = self.hash(key)
        node = self.buckets[hashed_key]
        if node is None:
            return
        while True:
            if node.key == key:
                return node
            if node.next is None:
                break
        return

    def delete (self, key):
        hashed_key = self.hash(key)
        node = self.buckets[hashed_key]
        prev_node = None
        if node is None:
            return False
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.buckets[hashed_key] = node.next
                prev_node.next = node.next
                return node

            prev_node = node
            node = node.next
        return

        

ht = HashTable()
ht.insert("myKey", "myValue")       #hash key = 1
ht.insert("test0", "test0->123")    #hash key = 1
ht.insert("test1", "test1->123")
ht.insert("test2", "test2->123")    #hash key = 1
ht.insert("test3", "test3->123")
ht.insert("test4", "test4->123")    #hash key = 1
ht.insert("test5", "test5->123")
ht.insert("test6", "test6->123")    #hash key = 1
ht.insert("test7", "test7->123")
ht.delete("test2")                  #deleted from hash bucket 1
print(ht.get("myKey"))
        
