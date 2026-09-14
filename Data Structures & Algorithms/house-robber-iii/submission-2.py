# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # feel like this is a dp problem
        def dfs(node):
            if not node:
                return 0, 0

            # print(self.rob(node.left))
            leftRob, leftSkip = dfs(node.left)
            rightRob, rightSkip = dfs(node.right)
            # print(node.val)
            # print(leftRes, robLeft)
            # print(rightRes, robRight)

            return node.val + leftSkip + rightSkip, max(leftRob, leftSkip)+max(rightRob, rightSkip)

        return max(dfs(root))

