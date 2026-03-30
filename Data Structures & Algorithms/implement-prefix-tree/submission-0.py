class PrefixTree:

    def __init__(self):
        self.unique_words = set()
        self.prefix = set()
        

    def insert(self, word: str) -> None:
        for i in range(len(word) + 1):
            self.prefix.add(word[:i])
        self.unique_words.add(word)


    def search(self, word: str) -> bool:
        return word in self.unique_words
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix
        
        