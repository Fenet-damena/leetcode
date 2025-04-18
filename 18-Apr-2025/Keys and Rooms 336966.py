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
            for key in rooms[node]:
                if key not in visited:
                    que.append(key)
        return len(visited) == n
        