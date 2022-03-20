def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # if digits == [0]:
        #     return [1]
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        print(digits, i)
        if i == -1:
            digits = [1] + digits
        else:
            digits[i] += 1
        return digits

print(plusOne([0]))