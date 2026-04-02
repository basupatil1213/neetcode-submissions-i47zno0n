class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval[0], newInterval[1]
        
        for i, itr in enumerate(intervals):
            if itr[1] < start:
                res.append(itr)
            elif itr[0] > end:
                res.append([start, end])
                return res + intervals[i:]
            else:
                start = min(start, itr[0])
                end = max(end, itr[1])
        res.append([start, end])
        return res