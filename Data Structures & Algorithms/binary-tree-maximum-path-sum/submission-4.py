# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # path: left subpath + parentNode + right subpath
        self.res = float("-inf")
        def dfs(node):
            if not node:
                return float("-inf")
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            self.res = max(self.res, leftSum + node.val, rightSum+node.val, leftSum + rightSum + node.val, node.val)
            return max(node.val, leftSum+node.val, rightSum+node.val)

        dfs(root)
        return self.res