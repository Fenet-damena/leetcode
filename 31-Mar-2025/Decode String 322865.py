# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
            st, num = [], []
            cur, n = "", 0
            
            for c in s:
                if c.isdigit():
                    n = n * 10 + int(c)
                elif c == "[":
                    st.append(cur)
                    num.append(n)
                    cur, n = "", 0
                elif c == "]":
                    cur = st.pop() + num.pop() * cur
                else:
                    cur += c
            
            return cur
                