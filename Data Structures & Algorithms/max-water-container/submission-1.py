class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0

        l, r = 0, len(heights) - 1

        while l < r:
            curr_water = min(heights[l], heights[r]) * (r - l)
            most_water = max(most_water, curr_water)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return most_water
        