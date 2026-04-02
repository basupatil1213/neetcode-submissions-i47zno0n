class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]

        res = []

        for i, itr in enumerate(intervals):
            if itr[0] > end:
                res.append([start, end])
                start = itr[0]
                end = itr[1]
            else:
                end = max(end, itr[1])
        res.append([start, end])
        
        return res