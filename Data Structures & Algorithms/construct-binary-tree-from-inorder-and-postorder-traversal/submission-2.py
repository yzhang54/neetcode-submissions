# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: left - root - right
        # postorder: left - right - root 

        # get root from postorder, and find the root in inorder, from there we find left and right, i am little stuck bc i am not sure when i do dfs, which traversal pattern should i do 
        if not inorder and not postorder:
            return None 
        curNode = TreeNode(postorder[-1])
        rootIndex = inorder.index(postorder[-1])
        leftSize = len(inorder[:rootIndex])
        rightSize = len(inorder[rootIndex+1:])

        curNode.left = self.buildTree(inorder[:rootIndex], postorder[:leftSize]) # left
        curNode.right = self.buildTree(inorder[rootIndex+1:], postorder[leftSize:len(postorder)-1]) # right 

        return curNode 
