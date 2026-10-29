"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj={}
        def dfs(node):
            if node in adj:
                return adj[node]
            adj[node]=Node(node.val)
            for n in node.neighbors:
                adj[node].neighbors.append(dfs(n))
            return adj[node]
        return dfs(node) if node else None
        

        

            
        