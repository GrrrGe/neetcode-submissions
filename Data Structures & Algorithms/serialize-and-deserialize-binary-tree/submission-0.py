# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = ""
        def dfs(root):
            nonlocal ser
            if not root:
                ser+="N,"
                return
            
            ser+=str(root.val)+","
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(ser[:-1])
        return ser[:-1]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        stream = data.split(",")
        self.i = 0
        def dfs():
            if self.i>=len(stream):
                return None
            if stream[self.i]=="N":
                self.i+=1
                return None
            val = int(stream[self.i])
            node = TreeNode(val)
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

            

        
