# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.head = None
        self.que = deque()
        self.next = None
        

    def push(self, x: int) -> None:
        self.que.append(x)
        

    def pop(self) -> int:
        remove = self.que.popleft()
        return remove
        

    def peek(self) -> int:
        if self.que:
          app =self.que[0]
          return app
        return None
        
        
        

    def empty(self) -> bool:
        if self.que:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()