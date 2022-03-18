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

# x = 16
# print((x ^ (x - 1)).bit_length() - 1)
# print([i for i in range (5)])

nums = [1,1]
arr = [i for i in range(1, len(nums)+1)]
for num in nums:
    arr[num-1] = None
print ([j for j in arr if j is not None])