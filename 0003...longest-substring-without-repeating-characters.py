class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        frm, mx = 0, 0
        for ch in s:
            if(ch in st):
                mx = max(mx, len(st))
                index = s.find(ch, frm)
                for i in range(frm, index+1):
                    st.discard(s[i])
                frm = index+1
            st.add(ch)
        return max(mx, len(st))
