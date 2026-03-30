class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(node):
            if not graph[node] or node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        connected_graphs = 0
        for i in range(n):
            if i not in visited:
                connected_graphs += 1
                dfs(i)
        
        return connected_graphs
        