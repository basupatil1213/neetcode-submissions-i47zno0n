class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        res = 0

        for num in nums:
            if num - 1 not in unique_nums:
                curr = 1
                seq = num
                while seq + 1 in unique_nums:
                    curr += 1
                    seq += 1
                
                res = max(res, curr)
        
        return res