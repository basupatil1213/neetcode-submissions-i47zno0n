class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        for i in range(len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            res = s[l + 1 : r] if len(res) < (r - l - 1) else res

            l = i
            r = i + 1

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            res = s[l + 1 : r] if len(res) < (r - l - 1) else res
        
        return res
        
        