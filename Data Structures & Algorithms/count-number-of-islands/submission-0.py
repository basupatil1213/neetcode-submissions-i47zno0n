class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        islands = 0
        def helper(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == "0":
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            helper(i +1, j)
            helper(i - 1, j)
            helper(i, j + 1)
            helper(i, j - 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    helper(i, j)
        
        return islands
        