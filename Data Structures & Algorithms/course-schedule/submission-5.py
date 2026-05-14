class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prequisites problem
        # dfs -> for each node exhaust prereq until base case

        seen = set()
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False # cycle
            if adj[crs] == []:
                return True # no prereq base case

            seen.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            seen.remove(crs)
            adj[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


