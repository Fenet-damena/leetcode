# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        heap = []
        heapq.heapify(heap)

        for key , v in c.items():
                heapq.heappush(heap, (-v,key))
        ans = []

        for i in range(k):
            frq, word = heapq.heappop(heap)
            ans.append(word)
        return ans
          
        