# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            return TreeNode(val)

        def dfs(node, val):
            if node == None:
                return None

            if val < node.val:
                if not dfs(node.left, val):
                    node.left = TreeNode(val)
            else:
                if not dfs(node.right, val):
                    node.right = TreeNode(val)

            return node

        dfs(root, val)

        return root
