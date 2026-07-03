class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def helper(curr, i):
            if i == len(nums):
                res.append(curr)
                return
            helper(curr, i + 1)
            helper(curr ^ nums[i], i + 1)
        helper(0, 0)
        return sum(res)