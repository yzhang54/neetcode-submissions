class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        
        curNode = self.root

        for letter in word:
            if letter in curNode.children:
                curNode = curNode.children[letter]
            else:
                curNode.children[letter] = Node()
                curNode = curNode.children[letter]

        curNode.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(index, curNode): # we wanna search word in the tree
            # base:
            if index >= len(word):
                return curNode.isEnd

            letter = word[index]
            # option 1: match the letter
            if letter in curNode.children:
                if dfs(index+1, curNode.children[letter]):
                    return True
            # option 2: match dot, trying all children
            if letter == ".":
                for letter, node in curNode.children.items():
                    if dfs(index+1, node):
                        return True

            return False

        return dfs(0, self.root)


