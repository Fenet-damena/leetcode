# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Node(homepage)  

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.val
