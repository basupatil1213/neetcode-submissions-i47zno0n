class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def helper(i, last_idx):
            if i >= last_idx:
                return 0
            if i in memo:
                return memo[i]
            with_house = nums[i] + helper(i + 2, last_idx)
            without_house = helper(i + 1, last_idx)
            memo[i] = max(with_house, without_house)
            return memo[i]
        first = helper(0, len(nums) - 1)
        memo = {}
        second = helper(1, len(nums))
        return max(first, second)

        