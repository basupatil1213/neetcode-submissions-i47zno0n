class TrieNode:
    def __init__(self):
        self.childrens = [None]*26
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.childrens[index] is None:
                curr.childrens[index] = TrieNode()
            curr = curr.childrens[index]
        
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)
    
    def _dfs(self, word, i, node):
        if i == len(word):
            return node.endOfWord
        
        if word[i] == '.':
            for child in node.childrens:
                if child and self._dfs(word, i + 1, child):
                    return True
            return False
        else:
            index = ord(word[i]) - ord('a')
            if node.childrens[index] is None:
                return False
            return self._dfs(word, i + 1, node.childrens[index])
        
