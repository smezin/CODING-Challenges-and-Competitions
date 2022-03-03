def dec_2_bit(d):
    if d < 0 or d > 1:
        return 'Error'
    
    answer = '.'
    base = 0.5
    for i in range(32):
        print(i, d)
        if d  >= base:
            answer += '1'
            d -= base
            if d ==0:
                break
        else:
            answer += '0'
        base /= 2
    return answer

print(dec_2_bit(0.634765625))
