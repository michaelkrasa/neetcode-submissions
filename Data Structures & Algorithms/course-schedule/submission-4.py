class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap = defaultdict(list)
        visit = set() # detect repeat visits to set

        # prime our map
        for course, pre in prerequisites:
            crsMap[course].append(pre)

        # run dfs on
        def dfs(course):
            if course in visit:
                return False # cycle
            if crsMap[course] == []:
                return True

            visit.add(course)
            for pre in crsMap[course]:
                if not dfs(pre):
                    return False

            # we know course and all its prerequisites are valid
            visit.remove(course)
            crsMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

