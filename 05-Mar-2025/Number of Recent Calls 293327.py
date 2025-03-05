# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.req_count =  deque()
        

    def ping(self, t: int) -> int:

        while self.req_count  and t-self.req_count[0] > 3000:
            self.req_count.popleft()
        self.req_count.append(t)
        return len(self.req_count)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)