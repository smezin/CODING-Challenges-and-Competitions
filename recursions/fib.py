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

if __name__ == '__main__':
    m = fibonacci(16)
    print(m)
    print(fibs)