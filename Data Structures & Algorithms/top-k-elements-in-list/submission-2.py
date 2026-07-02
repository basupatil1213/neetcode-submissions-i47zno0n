from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        topK = []

        for key, value in counter.items():

            heappush(topK, (value, key))
            if len(topK) > k:
                heappop(topK)
        
        return [v for k, v in topK]
        