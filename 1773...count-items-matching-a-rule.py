class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = 0
        if ruleKey == 'color':
            idx = 1
        if ruleKey == 'name':
            idx = 2
        count = 0
        for i in items:
            if i[idx] == ruleValue:
                count += 1
        return count
