class Solution(object):
    def minWindow(self, s, p):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        if n < len(p):
            return ''
        desired_map = {}
        
        # Starting index of shortest_answer
        start = 0
        
        # Answer
        # Length of shortest_answer
        shortest_answer = n + 1
        uniques_counter = 0
        
        # creating map
        for ch in p:
            if ch in desired_map:
                desired_map[ch] += 1
            else: 
                desired_map[ch] = 1
            if desired_map[ch] == 1:
                uniques_counter += 1
                
        # References of Window       
        right_runner = 0
        left_runner = 0
        print(f'desired:{desired_map}, uniques:{uniques_counter}')
        # Traversing the window
        while(right_runner < n):
            #move right runner
            if s[right_runner] in desired_map:
                desired_map[s[right_runner]] -= 1
                if desired_map[s[right_runner]] == 0:
                    uniques_counter -= 1        #letter count of one of chars in p went down to 0
                print(f'desired:{desired_map}, uniques:{uniques_counter}, j:{right_runner}')
                
                # enter here when all letters in desired map were found 
                while uniques_counter == 0:
                    if shortest_answer > right_runner - left_runner + 1:
                        shortest_answer = right_runner - left_runner + 1
                        start = left_runner
                        
                    # move left runner
                    if s[left_runner] in desired_map:
                        desired_map[s[left_runner]] += 1
                        if desired_map[s[left_runner]] > 0:
                            uniques_counter += 1
                    left_runner += 1
            right_runner += 1
        if shortest_answer > n:
            return ''
        return s[start:start+shortest_answer]
        

s = Solution()
k = s.minWindow('ADOBECODEBANC','ABC')
print(k)