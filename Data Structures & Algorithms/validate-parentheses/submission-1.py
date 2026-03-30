class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'}': '{', ')': '(', ']': '['}

        for char in s:
            if char not in matching:
                stack.append(char)
            else:
                if not stack or matching[char] != stack[-1]:
                    return False
                stack.pop()

        return not stack