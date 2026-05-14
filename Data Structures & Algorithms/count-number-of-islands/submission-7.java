class Solution {
    int ROWS;
    int COLS;
    static final int[][] DIRS = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    public int numIslands(char[][] grid) {
        ROWS = grid.length; 
        COLS = grid[0].length;
        
        int islands = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == '1') {
                    dfs(r, c, grid);
                    islands++;
                }
            }
        }
        return islands;
    }

    void dfs(int r, int c, char[][] grid) {
        if (0 <= r && r < ROWS && 0 <= c && c < COLS && grid[r][c] == '1') {
            grid[r][c] = '0';
            for (int[] dir : DIRS) {
                dfs(r + dir[0], c + dir[1], grid);
            }
        }
    }
}
