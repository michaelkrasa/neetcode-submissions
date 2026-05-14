class Solution:
    def checkIfPrerequisite(self, numCourses: int,
                            prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        preMap = {}  # crs -> set of all its prerequisites

        def dfs(crs):
            if crs in preMap:
                return preMap[crs]
            
            pres = set()
            for nei in adj[crs]:
                pres.add(nei)       # direct prereq
                pres |= dfs(nei)    # all prerequisites of that neighbor

            preMap[crs] = pres
            return pres

        # Build prerequisite sets for all courses
        for i in range(numCourses):
            dfs(i)

        # For each query (u, v): is u a prerequisite of v?
        return [u in preMap[v] for u, v in queries]
