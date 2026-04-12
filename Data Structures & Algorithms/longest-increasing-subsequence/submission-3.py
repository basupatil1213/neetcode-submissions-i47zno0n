import sys
sys.setrecursionlimit(10000)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def helper(i, prev):
            if i == len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            skip = helper(i + 1, prev)
            take = 0
            if nums[i] > prev:
                take = 1 + helper(i + 1, nums[i])
            
            memo[(i, prev)] = max(skip, take)
            return memo[(i, prev)]
            
        return helper(0, float('-inf'))