class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def bfs(r, c) -> int:
            q = deque([(r,c)])
            grid[r][c] = 0
            area = 0
            
            while q:
                r, c = q.popleft()
                area += 1
                
                # explore neighbors
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    # out of bounds or water -> contributes 0
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))

            return area

        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    best = max(best, bfs(r, c))
        return best
