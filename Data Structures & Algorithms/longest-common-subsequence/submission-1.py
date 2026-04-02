class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def helper(i, j, curr_len):
            if i >= len(text1) or j >= len(text2):
                return curr_len
            if (i, j, curr_len) in memo:
                return memo[(i, j, curr_len)]
            memo[(i, j, curr_len)] = helper(i + 1, j + 1, curr_len + 1) if text1[i] == text2[j] else max(helper(i, j + 1, curr_len), helper(i + 1, j, curr_len))
            return memo[(i, j, curr_len)]
        return helper(0,0,0)
                
            

            

        