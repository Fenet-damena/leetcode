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
            for k in rooms[node]:
                if k not in visited:
                    que.append(k)
        return len(visited) == n
        