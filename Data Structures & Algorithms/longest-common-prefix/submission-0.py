class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Insert first word
        curr = self.root
        for c in strs[0]:
            index = ord(c) - ord('a')
            curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.endOfWord = True

        # Prune trie using remaining words
        for word in strs[1:]:
            curr = self.root
            for c in word:
                index = ord(c) - ord('a')
                if curr.children[index] is None:
                    break                        # char not in first word, stop
                curr = curr.children[index]
            # ✅ Prune: cut off everything after this point
            curr.children = [None] * 26
            curr.endOfWord = True               # mark as new endpoint

        # Traverse until a dead end or branch
        idx = 0
        curr = self.root
        while True:
            non_null = [c for c in curr.children if c is not None]
            if len(non_null) != 1 or curr.endOfWord:
                break
            idx += 1
            curr = non_null[0]

        return strs[0][:idx]