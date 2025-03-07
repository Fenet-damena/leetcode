# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.que = deque()
        self.count = 0  
        
    def consec(self, num: int) -> bool:
        if  len(self.que) == self.k:
            remove = self.que.popleft()
            if remove == self.value:
                self.count -= 1
        self.que.append(num)
        if num == self.value:
            self.count += 1

        return self.count == self.k
