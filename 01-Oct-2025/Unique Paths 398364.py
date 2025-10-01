# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(cor):
            r , c = cor
            if cor == (m - 1,n - 1):
                return 1
            ans = 0
            if r + 1 < m:
               ans += dp((r + 1, c))
            if c + 1 < n:
               ans += dp((r, c + 1))
            return ans

        return dp((0,0))
