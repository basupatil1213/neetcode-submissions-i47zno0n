class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]

        for i in range(1, len(nums)):
            temp = max_prod
            max_prod = max(nums[i], nums[i] * max_prod, nums[i] * min_prod)
            min_prod = min(nums[i], nums[i] * temp, nums[i] * min_prod)
            res = max(res, max_prod)
        return res