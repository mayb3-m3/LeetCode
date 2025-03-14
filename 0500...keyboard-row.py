class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans, f, s, t = [], "qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"
        for word in words:
            st = set()
            for letter in word:
                if letter in f:
                    st.add(1)
                elif letter in s:
                    st.add(2)
                else:
                    st.add(3)
            if len(st) == 1:
                ans.append(word)
        return ans
