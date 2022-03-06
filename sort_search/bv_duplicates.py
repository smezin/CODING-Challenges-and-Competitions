from BitVector import BitVector
from random import sample, randrange, randint

MAX_N = 32000

def solution (dups=1):
    bv = BitVector(size = MAX_N)
    lst = gen_input_list(dups)
    return mark_bv(lst, bv)

def mark_bv(lst, bv):
    for i in lst:
        bv[i] = 1 ^ bv[i]
    return get_dups(bv)

def get_dups(bv):
    dups = set()
    for i in range(len(bv)-1):
        if bv[i] == 0:
            dups.add(i)
    return dups

def gen_input_list(dups=1):
    size = randrange(MAX_N-1, MAX_N, 1)
    input =  list(sample(range(size), size))
    while dups > 0:
        input.append(randint(0, MAX_N))
        dups -= 1
    return input
    
#print(list(gen_input_list(3)))
print(solution(2))