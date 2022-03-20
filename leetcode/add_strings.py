def addStrings(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        carry = 0
        
        if len(num1) > len(num2):
            l, s = num1, num2
        else:
            l, s = num2, num1
            
        s = s.zfill(len(l))
        print(s,l)
        for i in range(len(l) - 1, -1, -1):
            a, b = int(l[i]), int(s[i])
            residue = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            print(f'a:{a} b:{b} carry:{carry} residue:{residue}')
            res.append(str(residue))
        if carry != 0:
            res.append(str(carry))
        res = res[::-1]
        res = ''.join(res)
        print(res)

addStrings('1', '9')