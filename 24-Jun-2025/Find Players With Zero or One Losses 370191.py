# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        l={}
        w={}
        for i in matches:
            if i[0] not in w:
                w[i[0]]=1
          
            else:
                w[i[0]]+=1
            if i[1] not in l:
                l[i[1]]=1
            else:
                l[i[1]]+=1
        ww=[]
        ll=[]
        
        for k,v in w.items():
            if k not in l:
                ww.append(k)
        for k in l:
            if l[k]==1:
                ll.append(k)
        ww.sort()
        ll.sort()
        return [ww,ll]
