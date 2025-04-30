# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones =[-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            flarge = -heapq.heappop(stones)
            slarge = -heapq.heappop(stones)

            if flarge != slarge:
                heapq.heappush(stones, -(flarge - slarge))
        return -stones[0] if  stones else 0
        

        