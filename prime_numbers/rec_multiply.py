#brute
def multiply_pos (a: int, b:int, res: int = 0, calls=0) -> int:
    if a <= 0 or b <= 0:
        return res
    if a > b:
        res += a
        b -= 1
    else:
        res += b
        a -= 1
    calls += 1
    print(calls)
    return multiply_pos(a, b, res, calls)

def multiply_pos1(a: int, b:int, res: int = 0) -> int:
    pass
