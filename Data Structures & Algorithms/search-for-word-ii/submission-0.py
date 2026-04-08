class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None  # stores full word at end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        # Step 1: Insert all words into Trie
        for word in words:
            curr = root
            for c in word:
                index = ord(c) - ord('a')
                if curr.children[index] is None:
                    curr.children[index] = TrieNode()
                curr = curr.children[index]
            curr.word = word  # store word at terminal node
        
        res = []
        rows, cols = len(board), len(board[0])

        # Step 2: DFS from every cell on the board
        def dfs(i, j, node):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            
            c = board[i][j]
            if c == '#':  # already visited
                return
            
            index = ord(c) - ord('a')
            if node.children[index] is None:  # no matching path in Trie
                return
            
            node = node.children[index]
            
            if node.word:
                res.append(node.word)
                node.word = None  # avoid duplicates
            
            board[i][j] = '#'  # mark visited
            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)
            board[i][j] = c  # restore
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        
        return res