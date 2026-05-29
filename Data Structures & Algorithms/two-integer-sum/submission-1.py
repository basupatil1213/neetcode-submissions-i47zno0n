class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_idx = {}

        for i in range(len(nums)):
            if nums[i] in value_idx:
                return [value_idx[nums[i]], i]
            value_idx[target - nums[i]] = i
        
        return [-1,-1]
        