class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        max_freq = 0
        result = 0
        l = 0

        for r in range(len(s)):
            char_count[s[r]] += 1
            max_freq = max(max_freq, char_count[s[r]])

            while (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result