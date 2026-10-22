class Node:
    def __init__(self, url=None, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        # double link list
        self.head = Node(homepage)
        self.tail = Node(None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.current = self.head

    def printList(self):
        print("----printList----")
        pointer = self.head
        while pointer != self.tail:
            print(pointer.url)
            pointer = pointer.next

    def visit(self, url: str) -> None:
        # print(url)
        # self.printList()
        # remove all forward pages, and add the new url page 
        self.current.next, self.tail.prev = None, None
        newPage = Node(url)
        self.current.next, newPage.prev = newPage, self.current
        self.tail.prev, newPage.next = newPage, self.tail
        self.current = self.current.next

        # self.printList()

    def back(self, steps: int) -> str:
        # self.printList()
        # check if length > x 
        while self.current != self.head:
            steps -= 1
            self.current = self.current.prev
            if steps == 0:
                return self.current.url
        
        return self.current.url

    def forward(self, steps: int) -> str:
        # check index 
        # move current poiinter 
        print(self.current.url)
        print(self.tail.prev)
        while self.current != self.tail.prev:
            steps -= 1
            self.current = self.current.next
            if steps == 0:
                return self.current.url

        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)