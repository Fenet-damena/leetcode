# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = [i for i in nums]
        heapq.heapify(heap)
        ans = 0
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x < k:
                sums =(min(x, y) * 2 + max(x, y))
                heapq.heappush(heap,sums)
                ans += 1
            else:
                return ans
                break
        return ans