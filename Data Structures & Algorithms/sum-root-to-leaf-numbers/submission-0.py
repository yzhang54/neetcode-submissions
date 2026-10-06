# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # find all paths from root to the leaves 
        res = []
        def dfs(curSum, node):
            if not node:
                return 

            # print(node.val)
            curSum = curSum*10 + node.val
            if not node.left and not node.right:
                print(node.val)
                res.append(curSum)

            dfs(curSum, node.left)
            dfs(curSum, node.right)

        
        dfs(0,root)
        print(res)
        return sum(res)
        

            

