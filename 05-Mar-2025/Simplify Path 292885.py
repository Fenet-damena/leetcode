# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        new_p = path.split("/")
        new_p = [i for i in new_p if i]
        simplified = []

        for i in new_p:
            if i == "..":
                if  simplified:
                   simplified.pop()
                    
            elif i == ".":
                continue
            else:
                simplified.append(i)
           
               

        return "/" +"/".join(simplified)


        