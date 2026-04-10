class TrieNode:
    def __init__(self):
        self.children = {}      # ✅ dict to handle multi-char folder names
        self.endOfPath = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort so parent folders always come before their subfolders
        folder.sort()
        res = []

        for f in folder:
            curr = self.root
            isSubFolder = False
            path = f.split('/')

            for p in path:
                if p == "":
                    continue
                if p not in curr.children:
                    curr.children[p] = TrieNode()
                
                curr = curr.children[p]  # ✅ move into child first

                if curr.endOfPath:       # ✅ then check if this is a recorded folder
                    isSubFolder = True
                    break

            if not isSubFolder:
                curr.endOfPath = True    # ✅ mark endpoint for valid folders
                res.append(f)

        return res