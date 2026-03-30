class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_ocean = set()
        atlantic_ocean = set()
        def helper(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))

            helper(r + 1, c, visit, heights[r][c])
            helper(r - 1, c, visit, heights[r][c])
            helper(r, c + 1, visit, heights[r][c])
            helper(r, c - 1, visit, heights[r][c])
        
        for r in range(rows):
            helper(r, 0, pacific_ocean, heights[r][0])
            helper(r, cols - 1, atlantic_ocean, heights[r][cols - 1])
        
        for c in range(cols):
            helper(0, c, pacific_ocean, heights[0][c])
            helper(rows - 1, c, atlantic_ocean, heights[rows - 1][c])
        
        res = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in atlantic_ocean and (i, j) in pacific_ocean:
                    res.append([i, j])
        
        return res
            


        