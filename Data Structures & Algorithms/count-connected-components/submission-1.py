class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Using dictionary for adjacency list
        graph = {}
        visit = set()
        # Initialize adjacency list
        for i in range(n):
            graph[i] = []
        # Populate adjacency list
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)  # Undirected graph

        # Depth First Search function
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        count = 0
        # Perform DFS on each unvisited node
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        return count
