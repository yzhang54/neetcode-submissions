class TreeNode:
    def __init__(self):
        self.children = {} # {"a": TreeNode}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curNode = self.root

        for letter in word:
            if letter in curNode.children:
                curNode = curNode.children[letter]
            else:
                curNode.children[letter] = TreeNode()
                curNode = curNode.children[letter]

        curNode.isEnd = True

    def search(self, word: str) -> bool:
        curNode = self.root

        for letter in word:
            if letter in curNode.children:
                curNode = curNode.children[letter]
            else:
                return False

        return curNode.isEnd == True
        

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root

        for letter in prefix:
            if letter in curNode.children:
                curNode = curNode.children[letter]
            else:
                return False

        return True
        