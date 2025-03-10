# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = 0

        for i in range(len(happiness)):
            if k > 0:
                if happiness[i] - i >=0:
                    ans += happiness[i]-i
                    k -= 1
                else:
                    ans += 0
        return ans


        