class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        can_reach = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= can_reach:
                can_reach = i
        
        return can_reach == 0
        