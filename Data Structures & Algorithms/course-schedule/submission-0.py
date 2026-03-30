class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_graph = [set() for _ in range(numCourses)]

        for preq in prerequisites:
            course, preq_course = preq[0], preq[1]
            preq_graph[course].add(preq_course)
        
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            
            if node in visited:
                return True
            
            path.add(node)
            for neighbor in preq_graph[node]:
                if not dfs(neighbor):
                    return False
            path.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True