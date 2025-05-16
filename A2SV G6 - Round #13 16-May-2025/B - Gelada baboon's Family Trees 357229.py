# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/607625/problem/B

class unionfind:
    def __init__(self, size):
        self.p = list(range(size))
        self.rank = [1]*size
    def find(self,x):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,x,y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx!=rooty:
            if self.rank[rootx]>self.rank[rooty]:
                self.p[rooty]=rootx
            elif self.rank[rootx]<self.rank[rooty]:
                self.p[rootx]=rooty
            else:
                self.p[rooty]=rootx
                self.rank[rootx]+=1
num=int(input())
l = list(map(int,input().split()))

uninF = unionfind(num)
for i in range(num):
    uninF.union(i,l[i]-1)
group = set()
for i in range(num):
    group.add(uninF.find(i))
print(len(group))
