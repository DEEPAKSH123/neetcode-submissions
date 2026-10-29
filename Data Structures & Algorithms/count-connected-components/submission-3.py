class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        visited = set()

        # Initialize adjacency list
        for i in range(n):
            graph[i] = []

        # Populate adjacency list
        in_degree = [0] * n  # Track in-degree of each node
        for a, b in edges:
            graph[a].append(b)  # Directed graph
            in_degree[b] += 1

        # Find nodes with in-degree zero to start DFS
        start_nodes = [i for i in range(n) if in_degree[i] == 0]

        # Depth First Search function
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        count = 0
        # Perform DFS on each start node
        for node in start_nodes:
            if node not in visited:
                dfs(node)
                count += 1

        # For any remaining unvisited nodes, they might be in isolated cycles
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count