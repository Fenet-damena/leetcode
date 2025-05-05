# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        reachable = [[False] * numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            graph[pre].append(course)

        def dfs(start, node):
            for neighbor in graph[node]:
                if not reachable[start][neighbor]:
                    reachable[start][neighbor] = True
                    dfs(start, neighbor)

        for i in range(numCourses):
            dfs(i, i)

        return [reachable[u][v] for u, v in queries]
