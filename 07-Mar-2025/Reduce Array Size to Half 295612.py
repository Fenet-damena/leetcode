# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        c = Counter(arr)
        st =set()
        leng =len(arr)
        c = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))

        for k ,v in c.items():
            leng -= v
            st.add(k)

            if leng <= len(arr)//2:
                return len(st)





        