# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c= Counter()

        for visit in cpdomains:
            
            frq,web = visit.split(' ')
            dom = web.split('.')
            for i in range(len(dom)):
                c['.'.join(dom[i:])] += int(frq)

        resualt = []
        for web,frq in c.items():
              resualt.append(str(frq)+' '+ web)

        return   resualt



            
        