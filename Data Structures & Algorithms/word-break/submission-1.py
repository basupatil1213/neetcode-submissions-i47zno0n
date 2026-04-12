class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False
class Solution:

    def __init__(self):
        self.root = TrieNode()

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # create Trie
        for word in wordDict:
            curr = self.root
            for c in word:
                index = ord(c) - ord('a')
                if curr.children[index] is None:
                    curr.children[index] = TrieNode()
                curr = curr.children[index]
            curr.endOfWord = True
        memo = {}
        def helper(i, node):
            if i == len(s):
                return node.endOfWord
            if (i, node) in memo:
                return memo[(i, node)]
            res = False
            if node.endOfWord:
                res = helper(i, self.root)
            
            if node.children[ord(s[i]) - ord('a')] is not None:
                res = res or helper(i + 1, node.children[ord(s[i]) - ord('a')])
            memo[(i, node)] = res
            return memo[(i, node)]
        
        return helper(0, self.root)
        
        