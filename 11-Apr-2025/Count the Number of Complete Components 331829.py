# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = [False] * n

        def dfs(node, com):
            visited[node] = True
            com.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, com)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                com = []
                dfs(i, com)
                comp_size = len(com)
                is_complete = True
                for node in com:
                    if len(graph[node]) != comp_size - 1:
                        is_complete = False
                        break
                if is_complete:
                    count += 1
        
        return count

        