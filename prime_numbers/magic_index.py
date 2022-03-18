from typing import List


A = [-10, -5, 2, 2, 5 ,12]

def find_magic(s_array: List[int]):
    right = 0
    left = len(s_array) 
    return _find_magic(s_array, right, left)

def _find_magic(s_array: List[int], right: int, left: int) -> int:
    mid = (left + right) // 2
    if s_array[mid] == mid:
        print(mid)
        return mid
    if len(s_array[right:left]) == 1:
        print(-1)
        return -1
    print(f'arr:{s_array[right:left]}, mid:{mid}, right:{right}')
    if s_array[mid] < mid:
        _find_magic(s_array, mid, left)
    else:
        _find_magic(s_array, right, mid)

find_magic(A)