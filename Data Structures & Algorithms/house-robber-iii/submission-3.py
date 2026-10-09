# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, 0

            leftRob, leftNotRob = dfs(node.left)
            rightRob, rightNotRob = dfs(node.right)

            robNode = node.val + leftNotRob + rightNotRob
            notRobNode = max(leftRob + rightRob, leftNotRob + rightNotRob, leftRob + rightNotRob, rightRob + leftNotRob)
            print(node.val)
            print("robNode :", robNode)
            print("leftNotRob :", leftNotRob)
            print("rightNotRob :", rightNotRob)
            print("notRobNode :", notRobNode)
            print("leftRob :", leftRob)
            print("rightRob :", rightRob)
            return robNode, notRobNode

        return max(dfs(root))
