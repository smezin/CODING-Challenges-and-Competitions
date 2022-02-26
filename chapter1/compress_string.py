
def compress(s):
    output = []
    if len(s) < 3:
        return s
    counter = 1 
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            counter += 1
        else:
            partial_string = s[i-1] + str(counter)
            if counter > 1:
                output.append(partial_string)
                counter = 1
                if len(output) >= len(s):
                    return s                
            else:
                output.append(s[i])
    if counter > 1:
        output.append(s[i-1] + str(counter))
        counter = 1
        if len(output) >= len(s):
            return s      
    else:
        output.append(s[i])
    return ''.join(output)

print (compress('aaabbbaavvv'))