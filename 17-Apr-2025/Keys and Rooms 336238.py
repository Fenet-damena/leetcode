# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        n = len(rooms)

        que = deque([0])

        while que:
            node = que.popleft()
            if node in visited:
                continue
            visited.add(node)
            for i in rooms[node]:
                if i not in visited:
                    que.append(i)
        return len(visited) == n
        