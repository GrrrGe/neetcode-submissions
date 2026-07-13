class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.children[ord(c)-ord('a')]:
                cur.children[ord(c)-ord('a')] = TrieNode()
            cur = cur.children[ord(c)-ord('a')]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            if word[i]=='.':
                for child in cur.children:
                    if child and self.matchRest(child,word[i+1:]):
                        return True
                return False
            elif cur.children[ord(word[i])-ord('a')]:
                cur = cur.children[ord(word[i])-ord('a')]
            else:
                return False
        return cur.endOfWord

    def matchRest(self,root,word) -> bool:
        for i in range(len(word)):
            if word[i]=='.':
                for child in root.children:
                    if child and self.matchRest(child,word[i+1:]):
                        return True
                return False
            elif root.children[ord(word[i])-ord('a')]:
                root = root.children[ord(word[i])-ord('a')]
            else:
                return False
        return root.endOfWord

        
