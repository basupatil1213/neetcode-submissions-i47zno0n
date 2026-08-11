class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr_pref = 1
        res = []
        for num in nums:
            res.append(curr_pref)
            curr_pref *= num
        
        curr_pref = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= curr_pref
            curr_pref *= nums[i]
        
        return res
