# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1=Counter(s1)
        c2=Counter(s2)
        if c1 !=c2:
            return False
        else:
            d=0

            for r in range(len(s1)):
                if s1[r]!=s2[r]:
                    d+=1
            if d<3:
                return True
            return False
        