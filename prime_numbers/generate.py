
def bits_primes_generator(m):
    flags = 3                   #0000...00000011
    flags = set_bit(flags, m+2) #1000...00000011
    current_prime = 0
    search_runner = current_prime
    while search_runner < m:
        if not get_bit(flags, search_runner):
            current_prime = search_runner
            yield current_prime
            for i in range(current_prime*2, m+1, current_prime):
                flags = set_bit(flags, i)
            #print("{0:b}".format(flags))
        search_runner += 1

def get_bit(n, i):
    return (n & 1<<i) != 0

def set_bit(n, i):
    return (n | 1<<i)

def clear_bit(n ,i):
    mask = ~(1<<i)
    return n & mask

generator = bits_primes_generator(2**20)

for i in generator:
    print(i)
   