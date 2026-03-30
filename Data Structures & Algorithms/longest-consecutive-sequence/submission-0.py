class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_len = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in unique:
                curr_len = 0
                curr_val = nums[i]
                while curr_val in unique:
                    curr_len += 1
                    curr_val += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len
        