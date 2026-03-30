class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjecent = [set() for i in range(n)]

        for edge in edges:
            adjecent[edge[0]].add(edge[1])
            adjecent[edge[1]].add(edge[0])
        
        path = set()
        visited = set()
        def dfs(node, parent_node):
            if node in path:
                return False

            path.add(node)
            for child in adjecent[node]:
                if child == parent_node:
                    continue
                if not dfs(child, node):
                    return False
            visited.add(node)
            path.remove(node)
            return True
        
        return dfs(0, -1) and len(visited) == n
        

        