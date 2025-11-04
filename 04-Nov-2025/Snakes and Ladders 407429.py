# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [0]*(n*n+1)
        idx = 1
        for i in range(n-1, -1, -1):
            row = board[i] if (n-1-i) % 2 == 0 else board[i][::-1]
            for val in row:
                arr[idx] = val
                idx += 1
        
        q = deque([(1, 0)])
        vis = set([1])
        while q:
            cur, step = q.popleft()
            if cur == n*n:
                return step
            for i in range(1, 7):
                nxt = cur + i
                if nxt <= n*n:
                    if arr[nxt] != -1:
                        nxt = arr[nxt]
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append((nxt, step+1))
        return -1
        