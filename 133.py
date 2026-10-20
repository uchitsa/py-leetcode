"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        return self.dfs(node)

    def dfs(self, node, clonemap={}):
        if node in clonemap:
            return clonemap[node]
        clone = Node(node.val)
        clonemap[node] = clone
        for n in node.neighbors:
            cloneneig = self.dfs(n, clonemap)
            clone.neighbors.append(cloneneig)
        return clone
