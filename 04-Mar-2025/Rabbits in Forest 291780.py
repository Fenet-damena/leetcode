# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter()
        ans = 0

        for i in range(len(answers)):
            if answers[i] != 0:
                c [answers[i]] +=1
                if c [answers[i]] == answers[i] + 1: 
                    ans += c [answers[i]]
                    del c [answers[i]]
        for k , v in c.items():
            ans += k+1
        return ans + answers.count(0)
        

        