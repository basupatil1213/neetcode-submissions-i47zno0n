class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(rows):
            for j in range(cols//2):
                matrix[i][j], matrix[i][cols - j - 1] = matrix[i][cols - j - 1], matrix[i][j]
        
        