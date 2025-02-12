from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ddct = defaultdict(list)
        for s in strs:
            ddct["".join(sorted(list(s)))].append(s)
        ans = list()
        for i in ddct.values():
            ans.append(i)
        return ans
