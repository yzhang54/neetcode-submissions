class Node:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.curSize = 0
        self.k = k
        self.front = Node()
        self.rear = Node()
        self.front.next, self.rear.prev = self.rear, self.front

    def printList(self):
        curNode = self.front
        print("stating printing list")
        while curNode:
            print("curNode val", curNode.val)
            curNode = curNode.next
        print("ending printing list")
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        curNode = self.rear.prev
        newNode = Node(value)
        curNode.next, newNode.prev = newNode, curNode
        self.rear.prev, newNode.next = newNode, self.rear
        self.curSize += 1
        # self.printList()
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # self.printList()
        curNode = self.front.next
        nextNode = curNode.next
        self.front.next, nextNode.prev = nextNode, self.front
        self.curSize -= 1

        return True

    def Front(self) -> int:
        if self.curSize == 0:
            return -1
        # self.printList()
        return self.front.next.val

    def Rear(self) -> int:
        if self.curSize == 0:
            return -1

        return self.rear.prev.val

    def isEmpty(self) -> bool:
        
        return True if self.curSize == 0 else False

    def isFull(self) -> bool:
        return True if self.curSize == self.k else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()