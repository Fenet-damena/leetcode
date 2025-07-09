# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        notcom = ""
        com = False
        ans = []

        for l in source:
            i = 0
            while i < len(l):
                if com :
                    if l[i:i+2] == "*/":
                        com = False
                        i += 2
                    else:
                        i += 1
                else:
                    if l[i:i+2] == "/*":
                        com = True
                        i += 2
                    elif l[i:i+2] == "//":
                        break
                    else:
                        notcom += l[i]
                        i += 1
            if not com and notcom:
                ans.append(notcom)
                notcom = ""
        return ans
            
                        


