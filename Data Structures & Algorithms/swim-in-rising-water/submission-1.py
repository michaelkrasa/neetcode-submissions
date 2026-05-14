class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # build adj dict from this
        N = len(grid)
        seen = set()
        seen.add((0,0))

        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        heap = [[grid[0][0], 0, 0]] # time, r,c

        while heap:
            t, r, c = heapq.heappop(heap)
            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in seen:
                    # calc max t along the way
                    maxT = max(t, grid[nr][nc])
                    seen.add((nr,nc))
                    heapq.heappush(heap, [maxT, nr, nc])


