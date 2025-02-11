import re
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            start, end = 0, 0
            try:
                something = re.search(part, s)
                start, end = something.start(), something.end()
            except:
                break
            s = s[:start] + s[end:]
        return s
