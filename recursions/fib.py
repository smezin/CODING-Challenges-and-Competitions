fibs=[]

def fibonacci (n):
    return _fibonacci(n, [0]*(n+1))

def _fibonacci (i, memo, m=[]):
    if i == 0 or i == 1:
        return i
    if memo[i] == 0:
        memo[i] = _fibonacci(i-1, memo) + _fibonacci(i-2, memo)
        fibs.append(memo[i])
    return memo[i]


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    m = fibonacci(16)
    print(m)
    print(fibs)
    fib_list = fib(1000)
    for n in fib_list:
        print(n)