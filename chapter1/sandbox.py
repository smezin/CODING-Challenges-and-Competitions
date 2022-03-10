from random import sample


#Flatanning list of lists
NESTED = [[1,2],[3,4,5,6],[7],[8,8]]
flat = [n for sublist in NESTED for n in sublist]

i = 1
#print(sample(range(1,10), 9))

class ListContainer:
    def __init__(self):
        self.list = []
        self.size = len(self.list)
    def insert(self, i):
        self.list.append(i)


l = ListContainer()
print (l.size)
l.insert(1)
print (l.size)

print(ord('a'), ord('z'))