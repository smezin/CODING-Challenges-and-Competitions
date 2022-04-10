from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            print(f'lo:{lo}, mid:{mi}, hi:{hi}')
            print(f'comparing:{arr[mi]}({mi}) and:{arr[mi+1]}({mi+1})')
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo

k = peakIndexInMountainArray([1,22,3,4,5,6,7,0,0])
print(k)