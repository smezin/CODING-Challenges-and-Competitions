from random import sample


#Flatanning list of lists
NESTED = [[1,2],[3,4,5,6],[7],[8,8]]
flat = [n for sublist in NESTED for n in sublist]

i = 1
print(sample(range(1,10), 9))