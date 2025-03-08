# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c = Counter(blocks[:k])
        ans = c["W"]
        l = 0

        for i in range(k,len(blocks)):

            
            c[blocks[l]] -= 1
            if c[blocks[l]] == 0:
                del c[blocks[l]]
            l +=1
            c[blocks[i]] +=1
            ans = min(ans,c["W"])
        return ans


        