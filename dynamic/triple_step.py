N = 12
calls = 0
def steping_perms (n):
    global calls
    calls +=1
    if n < 0:
        return 0
    if n == 0:
        return 1
    return steping_perms(n-1)+steping_perms(n-2)+steping_perms(n-3)
    
# print('perms:', steping_perms(N))
# print ('calls:',calls)
calls = 0
print('-'*16)
def get_perms(n):
    memo = [-1]*(n+1)
    return _get_perms(n, memo)


def _get_perms(n, memo):
    global calls
    calls +=1
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] == -1:
        memo[n] = _get_perms(n-1, memo) + _get_perms(n-2, memo) + _get_perms(n-3, memo)
    return memo[n]

print('perms:', get_perms(N))
print ('calls:',calls)
