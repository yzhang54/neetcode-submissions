# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        leftToRight = True

        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            qCopy = list(q)

            tmp = []
            for i in range(size):
                curNode = q.popleft()
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)

                if leftToRight:
                    tmp.append(curNode.val)
                else:
                    tmp.append(qCopy[size - i - 1].val)

            res.append(tmp[:])


            leftToRight = not leftToRight

        return res

    