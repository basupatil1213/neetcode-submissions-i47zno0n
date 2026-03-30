class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        min_heap = []
        counter = Counter(nums)

        for key, value in counter.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [pair[1] for pair in min_heap]
        