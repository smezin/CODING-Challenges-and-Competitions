#brute force
class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        paths = 1
        for i in range(len(arr)):
            print(f'start: {i}')
            next = self.next_from_odd(i, arr)
            print(f'next00: {next}')
            if next == (len(arr) - 1):
                paths += 1
                next = -1
            while next != -1:
                next = self.next_from_even(next, arr)
                print(f'next01: {next}')
                if next == (len(arr) - 1):
                    paths += 1
                    next = -1
                next = self.next_from_odd(next, arr)
                print(f'next02: {next}')
                if next == (len(arr) - 1):
                    paths += 1
                    next = -1
        return paths
            

    def next_from_odd(self, index: int, arr):
        if (index == -1):
            return -1
        next_bigger = None
        next_bigger_i = -1
        for i in range(index, len(arr)):
            if arr[i] == arr[index] and i > index:
                return i
            if arr[i] > arr[index]:
                if next_bigger is None or arr[i] < next_bigger:
                    next_bigger_i = i
                    next_bigger = arr[i]
        if next_bigger_i < index:
            return -1
        return next_bigger_i

    def next_from_even(self, index: int, arr):
        if (index == -1):
            return -1
        next_smaller = None
        next_smaller_i = -1
        for i in range(index, len(arr)):
            if arr[i] == arr[index] and i > index:
                return i
            if arr[i] < arr[index]:
                if next_smaller is None or arr[i] > next_smaller:
                    next_smaller_i = i
                    next_smaller = arr[i]
        if next_smaller_i < index:
            return -1
        return next_smaller_i

class Solution1(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        paths = 1
        jumps = []
        for i in range(len(arr)):
            jumps.append((self.next_from_even(i,arr), self.next_from_odd(i, arr)))
        
        for i in range(len(arr)):
            print(f'start: {i}')
            next = jumps[i][1]
            if next == (len(arr) - 1):
                paths += 1
                next = -1
            while next != -1:
                next = jumps[next][0]
                if next == (len(arr) - 1):
                    paths += 1
                    next = -1
                next = jumps[next][1]
                if next == (len(arr) - 1):
                    paths += 1
                    next = -1
        return paths


    def next_from_odd(self, index, arr):
        if (index == -1):
            return -1
        next_bigger = None
        next_bigger_i = -1
        for i in range(index, len(arr)):
            if arr[i] == arr[index] and i > index:
                return i
            if arr[i] > arr[index]:
                if next_bigger is None or arr[i] < next_bigger:
                    next_bigger_i = i
                    next_bigger = arr[i]
        if next_bigger_i < index:
            return -1
        return next_bigger_i

    def next_from_even(self, index, arr):
        if (index == -1):
            return -1
        next_smaller = None
        next_smaller_i = -1
        for i in range(index, len(arr)):
            if arr[i] == arr[index] and i > index:
                return i
            if arr[i] < arr[index]:
                if next_smaller is None or arr[i] > next_smaller:
                    next_smaller_i = i
                    next_smaller = arr[i]
        if next_smaller_i < index:
            return -1
        return next_smaller_i



s = Solution1()
x = s.oddEvenJumps([10,13,12,14,15])
x1 = s.oddEvenJumps([2,3,1,1,4])


print(x1)
