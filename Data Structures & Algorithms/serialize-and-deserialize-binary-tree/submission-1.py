# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("None")
                return 
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        # print(res)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataList = data.split(",")

        self.i = 0
        def dfs():
            if self.i >= len(dataList):
                return None
            if dataList[self.i] == "None":
                self.i += 1
                return None

            curNode = TreeNode(int(dataList[self.i]))
            self.i += 1
            curNode.left = dfs()
            curNode.right = dfs()

            return curNode

        return dfs()



        