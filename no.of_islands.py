class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island(x, y, r, c):
            if x < 0 or x>=r or y < 0 or y >= c or grid[x][y] != "1":
                return
            grid[x][y] = "0"
            island(x+1, y, r,c)
            island(x,y+1,r,c)
            island(x-1,y,r,c)
            island(x,y-1,r,c)
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0]) 
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    island(i,j, rows, cols)
        return count        