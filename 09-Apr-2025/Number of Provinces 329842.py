# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        ans = 0

        def dfs(c):
            for i in range(n):
                if isConnected[c][i] == 1 and  i not in visited:
                    visited.add(i)
                    dfs(i)
        for i in range(n):
            if i not in visited:
                ans +=1
                visited.add(i)
                dfs(i)
        return ans 