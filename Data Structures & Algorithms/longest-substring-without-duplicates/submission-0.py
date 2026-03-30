class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_idx = {}

        max_len = 0

        start_idx = 0

        for end_idx in range(len(s)):
            if s[end_idx] in char_idx and char_idx[s[end_idx]] >= start_idx:
                start_idx = char_idx[s[end_idx]] + 1
            char_idx[s[end_idx]] = end_idx
            max_len = max(max_len, end_idx - start_idx + 1)
        
        return max_len
            
        