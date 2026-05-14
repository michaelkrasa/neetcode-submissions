class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        on_path, done = set(), set()
        res = []

        def dfs(crs):
            if crs in on_path:
                return False  # cycle
            if crs in done:
                return True

            on_path.add(crs)
            for nei in prereq[crs]:
                if not dfs(nei):
                    return False
            on_path.remove(crs)
            done.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
