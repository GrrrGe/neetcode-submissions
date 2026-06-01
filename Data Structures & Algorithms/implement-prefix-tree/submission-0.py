class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                curr.children[ord(c)-ord('a')] = TrieNode()
            curr = curr.children[ord(c)-ord('a')]
        curr.endOfWord = True
            
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if curr.children[ord(c)-ord('a')]:
                curr = curr.children[ord(c)-ord('a')]
        return curr.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if curr.children[ord(c)-ord('a')]:
                curr = curr.children[ord(c)-ord('a')]
            else:
                return False
        return True

        
        