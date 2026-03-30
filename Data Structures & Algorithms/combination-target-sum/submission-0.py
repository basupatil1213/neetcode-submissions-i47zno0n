class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(curr, total, i):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            total += nums[i]
            curr.append(nums[i])
            helper(curr, total, i)
            total -= nums[i]
            curr.pop()
            helper(curr, total, i + 1)
        helper([], 0, 0)

        return res
        