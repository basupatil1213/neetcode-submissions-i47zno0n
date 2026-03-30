class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        result = 0
        l = 0

        for r in range(len(s)):
            char_count[s[r]] += 1

            while (r - l + 1) - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result
        