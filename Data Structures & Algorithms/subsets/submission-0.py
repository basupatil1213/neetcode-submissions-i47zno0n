class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            helper(i + 1, curr)
            curr.pop()
            helper(i + 1, curr)
        
        helper(0, [])
        return res
        