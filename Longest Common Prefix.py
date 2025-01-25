class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for s in strs:
            temp = ""
            for ch1, ch2 in zip(s, ans):
                if ch1 == ch2:
                    temp += ch1
                else:
                    break
            ans = temp
        return ans
