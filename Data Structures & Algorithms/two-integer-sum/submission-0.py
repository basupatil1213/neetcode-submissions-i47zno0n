class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem_idx = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in rem_idx:
                return [rem_idx[rem], i]
            
            rem_idx[nums[i]] = i
        