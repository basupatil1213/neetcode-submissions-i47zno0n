class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem_to_idx = {}

        for idx, num in enumerate(nums):
            rem = target - num
            if rem in rem_to_idx:
                return [rem_to_idx[rem], idx]
            
            rem_to_idx[num] = idx
        
        return [-1, -1]
        