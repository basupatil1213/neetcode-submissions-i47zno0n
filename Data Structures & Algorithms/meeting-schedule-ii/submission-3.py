"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        
        min_heap = []
        res = 0

        for interval in intervals:
            if not min_heap:
                res += 1
                heapq.heappush(min_heap, interval.end)
            elif interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, interval.end)
            else:
                res += 1
                heapq.heappush(min_heap, interval.end)
        
        return res
        