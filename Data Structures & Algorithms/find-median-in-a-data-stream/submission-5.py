from heapq import heappush, heappop, heappush_max, heappop_max
class MedianFinder:

    def __init__(self):
        self.first = []
        self.second = []
        

    def addNum(self, num: int) -> None:

        heappush_max(self.first, num)

        # step 2: fix ordering
        if self.first and self.second and self.first[0] > self.second[0]:
            heappush(self.second, heappop_max(self.first))

        # step 3: fix balance
        if len(self.first) > len(self.second) + 1:
            heappush(self.second, heappop_max(self.first))
        elif len(self.second) > len(self.first):
            heappush_max(self.first, heappop(self.second))
        

    def findMedian(self) -> float:
        if (len(self.first) + len(self.second)) % 2 == 0:
            median = (self.first[0] + self.second[0]) / 2
            return median
        else:
            return self.first[0] if len(self.first) > len(self.second) else self.second[0]
        
        