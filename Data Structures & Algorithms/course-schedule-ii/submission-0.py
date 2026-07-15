class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        res = []
        visited = set()
        added = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs]==[]:
                if crs not in added:
                    res.append(crs)
                    added.add(crs)
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            if crs not in added:
                res.append(crs)
                added.add(crs)
            visited.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res