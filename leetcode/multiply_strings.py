def multiplyStrings(num1, num2):
    partials = []
    for i in range(len(num2) - 1, -1, -1):
        partial = multiplySingleDigit(num1, num2[i])
        partial = partial + '0' * (len(num2) - 1 - i)
        partials.append(partial)
    total = '0'
    for p in partials:
        total = addStrings(total, p)
    return total.lstrip('0')

def multiplySingleDigit(num1, digit):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    res = []
    carry = 0
    for i in range(len(num1) - 1, -1, -1):
        a = int(num1[i])
        b = int(digit)
        residue = (a * b + carry) % 10
        carry = (a * b + carry) // 10
        res.append(str(residue))
    if carry != 0:
        res.append(str(carry))
    res = res[::-1]
    res = ''.join(res)
    return res

def addStrings(num1, num2):
    res = []
    carry = 0
    
    if len(num1) > len(num2):
        l, s = num1, num2
    else:
        l, s = num2, num1
        
    s = s.zfill(len(l))
    for i in range(len(l) - 1, -1, -1):
        a, b = int(l[i]), int(s[i])
        residue = (a + b + carry) % 10
        carry = (a + b + carry) // 10
        res.append(str(residue))
    if carry != 0:
        res.append(str(carry))
    res = res[::-1]
    res = ''.join(res)
    return(res)

s = multiplyStrings('11', '23')
print(s)