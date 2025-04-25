# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        que = deque()
        fresh = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    que.append((r, c, 0))
                elif grid[r][c] == 1:  
                    fresh += 1

        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        minutes = 0  
        while que:
            r, c, minutes = que.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    que.append((nr, nc, minutes + 1))

        return minutes if fresh == 0 else -1
