class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def helper(i, j, k, visited):

            if k >= len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            
            if board[i][j] != word[k]:
                return False
            
            if (i, j) in visited:
                return False
            visited.add((i, j))
            result = helper(i, j + 1, k + 1, visited) or helper(i, j - 1, k + 1, visited) or helper(i + 1, j, k + 1, visited) or helper(i - 1, j, k + 1, visited)
            visited.remove((i, j))
            return result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]  == word[0] and helper(i, j, 0, set()):
                    return True
        
        return False
