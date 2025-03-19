# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [0] *len(deck)
        q = deque(range(len(deck)))

        for  i in deck:
            n = q.popleft()
            ans[n] = i
            if q:
                q.append(q.popleft())
        return ans
        