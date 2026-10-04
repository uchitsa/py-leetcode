class Node:
    def __init__(self):
        self.childs = {}
        self.islast = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.childs:
                node.childs[c] = Node()
            node = node.childs[c]
        node.islast = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.childs:
                return False
            node = node.childs[c]
        return node.islast

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.childs:
                return False
            node = node.childs[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
