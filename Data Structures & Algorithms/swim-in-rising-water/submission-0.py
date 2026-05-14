class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # build adj dict from this
        dirs = [[1,0], [0, 1], [0,-1], [-1,0]]
        visit = set()
        n = len(grid)

        heap = [[grid[0][0], 0, 0]]
        visit.add((0, 0))

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    maxT = max(t, grid[nr][nc])
                    heapq.heappush(heap, [maxT, nr, nc])
                    visit.add((nr, nc))