class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        is_pos = n > 0
        n = abs(n)
        
        def pown(x: float, n: int) -> float:
            if n == 0:
                return 1.0
            t = pown(x, n // 2)
            if n % 2 == 0:
                print('tt',t*t, 'n',n)
                return t*t
            else:
                print('ttx',t*t*x, 'n',n)
                return t*t*x
            
        
        res = pown(x ,n)
        return res if is_pos else 1/res

s= Solution()
s.myPow(2,9)