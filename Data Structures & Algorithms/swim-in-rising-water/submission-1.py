from heapq import heappush, heappop
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]  # (time, row, col)
        visited = set()

        while heap:
            time, r, c = heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n and
                    0 <= nc < n and
                    (nr, nc) not in visited
                ):
                    heappush(
                        heap,
                        (max(time, grid[nr][nc]), nr, nc)
                    )