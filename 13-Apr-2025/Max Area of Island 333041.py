# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        max_area = 0

        def dfs(r,c):
            if c < 0 or r <0 or r >= row or c >= col or  grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1+  dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        return max_area
   


        