class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr *= nums[j]
                res = max(res, curr)
        
        return res