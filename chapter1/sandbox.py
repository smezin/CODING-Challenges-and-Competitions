from re import sub


#Flatanning list of lists
NESTED = [[1,2],[3,4,5,6],[7],[8,8]]
flat = [n for sublist in NESTED for n in sublist]
