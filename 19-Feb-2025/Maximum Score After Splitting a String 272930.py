# Problem: Maximum Score After Splitting a String - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        l=0
        lf=Counter()
        rt=Counter(s[1:])
        lf[s[l]]=1
        ans=0
        for r in range(1,len(s)):
            sc=lf["0"]+rt["1"]
            ans=max(ans,sc)
            l+=1
            lf[s[l]]+=1
            rt[s[l]]-=1
            if rt[s[l]]==0:
                del rt[s[l]]
        return ans



 