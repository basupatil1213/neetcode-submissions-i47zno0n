class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        matching = {'}' : '{', ')':'(', ']':'['}
        for i in range(len(s)):
            if s[i] in ('(', '{', '['):
                stack.append(s[i])
            
            else:
                if not stack:
                    return False
                if matching[s[i]] != stack[-1]:
                    return False
                stack.pop()

        return not stack 
                