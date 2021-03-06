
from collections import defaultdict


ALPHABET_SIZE = ord('z')-ord('a') + 1
OFFSET = ord('a')
class Node:
    def __init__(self, ch):
        self.value = ch
        self.is_end_of_word = False
        self.children = [None] * ALPHABET_SIZE
    
    def __str__(self):
        return str([n.value for n in self.children if n is not None])

class PrefixTree:
    def __init__(self):
        self.root = Node(None) 

    def __str__(self): #TODO dfs
        children = [n.value for n in self.root.children if n is not None]
        return str(children)

    def insert(self, word):
        node = self.root
        for ch in word:
            ch_index = ord(ch) - OFFSET
            if not node.children[ch_index]:
                node.children[ch_index] = Node(ch)
            node =  node.children[ch_index]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            ch_index = ord(ch) - OFFSET
            if not node.children[ch_index]:
                return False
            node = node.children[ch_index]
        return node.is_end_of_word

    def print_words(self):
        words = []
        visited = defaultdict(bool)
        def dfs(node, word):
            for child in node.children:
                if child is None or visited[child]:
                    continue
                word.append(child.value)
                if child.is_end_of_word:
                    words.append(''.join(word))
                    return
                else:
                    dfs(child, word)
                    word = word[:]
            return words
        print(dfs(self.root, []))

    def dfs(self, node):
        for i in range(ALPHABET_SIZE):
            if node.children[i]:
                print( node.children[i].value)
                self.dfs(node.children[i])


            
pt = PrefixTree()
pt.insert('abc')
pt.insert('pop')
print('srch->', pt.search('abdz'))
print('srch->', pt.search('abdaz'))

pt.print_words()
