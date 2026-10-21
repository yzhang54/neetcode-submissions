class Node:
    def __init__(self,key = None, val = None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: Node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    # def printLinkList(self):
    #     curNode = self.head.next
    #     while curNode:
    #         print("curNode.key",curNode.key)
    #         print("curNode.value)", curNode.val)
    #         curNode = curNode.next
    def insert(self, node):
        # print("insert node val", node.val)
        # print("insert tail", self.tail.val)
        prevNode = self.tail.prev
        prevNode.next, node.prev  = node, prevNode
        node.next, self.tail.prev = self.tail, node

    def delete(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        curNode = self.cache[key]
        self.delete(curNode)
        self.insert(curNode)

        # print("After get, linked List is")
        # self.printLinkList()
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # print("key", key, "value", value)
        if key in self.cache:
            self.cache[key].val = value
            self.delete(self.cache[key])
            self.insert(self.cache[key])
        else:
            if len(self.cache) + 1 > self.capacity:
                # print("head", self.head)
                # print("tail", self.tail.val)
                leastNode = self.head.next
                del self.cache[leastNode.key]
                self.delete(leastNode)

            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insert(newNode)
        
        # print("After put, linked List is")
        # self.printLinkList()

        
