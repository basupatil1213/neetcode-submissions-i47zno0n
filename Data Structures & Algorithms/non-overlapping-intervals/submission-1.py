class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        unique_intervals = 1
        for i, itr in enumerate(intervals):
            if itr[0] >= end:
                unique_intervals += 1
                end = itr[1]
        
        

        return len(intervals) - unique_intervals