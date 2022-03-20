def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        c = 0
        if len(a) > len(b):
            longer, shorter = a, b
        else:
            longer, shorter = b, a
        
        shorter = shorter.zfill(len(longer))

        for i in range(len(longer)-1, -1, -1):
            l = int(longer[i])
            s = int(shorter[i])
            print(l,s,c)
            if (l + s + c) % 2 == 0:
                res.append('0')
            else:
                res.append('1')
            if (l + s + c) >= 2:
                c = 1
            else:
                c = 0
        if c == 1:
            res.append('1')

        res = res[::-1]
        s = ''.join(res)
        print(s)
        return s

addBinary('1001', '111')