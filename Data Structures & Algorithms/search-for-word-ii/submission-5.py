class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])

        res = []

        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        def dfs(r,c,node):
            if r < 0 or r>= ROWS or c < 0 or c >= COLS:
                return

            ch = board[r][c]

            if ch == '#' or ch not in node.children:
                return
            
            board[r][c]='#'
            
            next_node = node.children[ch]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            
            dfs(r+1,c,next_node)
            dfs(r,c+1,next_node)
            dfs(r-1,c,next_node)
            dfs(r,c-1,next_node)

            board[r][c]=ch
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)
        
        return res