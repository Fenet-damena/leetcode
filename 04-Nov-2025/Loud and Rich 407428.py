# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        for u, v in richer:
            g[v].append(u)
        ans = [-1]*n
        
        def dfs(x):
            if ans[x] != -1:
                return ans[x]
            ans[x] = x
            for y in g[x]:
                t = dfs(y)
                if quiet[t] < quiet[ans[x]]:
                    ans[x] = t
            return ans[x]
        
        return [dfs(i) for i in range(n)]
        