class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            rc = grid[r][c]
            grid[r][c] = 0

            up = dfs(r-1, c)
            down = dfs(r+1, c)
            left = dfs(r, c-1)
            right = dfs(r, c+1)

            return rc + up + down + left + right
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    if dfs(r, c) % k == 0:
                        count += 1
                    
        return count
