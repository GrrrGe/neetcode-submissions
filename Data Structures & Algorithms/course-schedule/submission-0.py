class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        

        def dfs(node,path)->bool:
            if node not in graph:
                return True
            if node in path:
                return False
            path.add(node)
            for child in graph[node]:
                if not dfs(child,path):
                    return False
            # path.remove(node)
            return True
        
        # count = 0
        for course in range(numCourses):
            if not dfs(course,set()):
                return False
        return True