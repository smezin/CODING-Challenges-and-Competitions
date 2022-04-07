from typing import List

def find_closest(values: List[int], target: int) -> int:
    if target < values[0]:
        return -1
    if target > values[-1]:
        return len(values) - 1
    
    left = 0
    right = len(values) 
    def bs (left: int, right: int):
        mid = left + (right - left) // 2
        if values[mid] == target:
            return mid
        elif mid == left:
            return left
        elif values[mid] > target:
            return bs(left, mid)
        elif values[mid] < target:
            return bs(mid, right)

    return bs(left, right)









V = [1,3,5,8,12,20]
print(find_closest(V, 0))