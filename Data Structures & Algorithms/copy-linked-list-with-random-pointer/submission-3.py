"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = defaultdict(Node)
        oldToCopy[None] = None
        curNode = head
        while curNode:
            copy = Node(curNode.val)
            oldToCopy[curNode] = copy
            curNode = curNode.next

        curNode = head
        while curNode:
            oldToCopy[curNode].next = oldToCopy[curNode.next]
            # print(curNode.random)
            oldToCopy[curNode].random = oldToCopy[curNode.random]
            curNode = curNode.next

        return oldToCopy[head]
        