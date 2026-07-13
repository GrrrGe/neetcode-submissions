class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.children[ord(c)-ord('a')]:
                node.children[ord(c)-ord('a')] = TrieNode()
            node = node.children[ord(c)-ord('a')]
        
        node.endOfWord = True



    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            node = node.children[ord(c)-ord('a')]
            if not node:
                return False
        return node.endOfWord
            
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            node = node.children[ord(c)-ord('a')]
            if not node:
                return False
        return True
        
        