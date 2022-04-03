
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return
        def get_next_closing(start: int) -> int:
            for i in range (start, len(s)):
                if s[i] == ']':
                    return i
        
        def get_bracket_mul(bracket: int) -> int:
            i = 1
            while s[bracket - i].isdigit():
                i += 1
            n = s[bracket - i + 1: bracket]
            return int(n)


        open_stack = []
        for idx, l in enumerate(s):
            if l == '[':
                open_stack.append(idx)
        
        while open_stack:
            start = open_stack.pop()
            end = get_next_closing(start)
            mul = get_bracket_mul(start)
            base_word = s[start + 1:end]
            processed_word = base_word * mul
            original = f'{mul}[{base_word}]'
            s = s.replace(original, processed_word)
        return s

I = '3[a2[c]]'
s = Solution()
s.decodeString(I)