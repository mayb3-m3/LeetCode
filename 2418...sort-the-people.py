class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr, ans = [], []
        for i in range(len(names)):
            arr.append((heights[i], names[i]))
        arr.sort(reverse = True)
        for i in arr:
            ans.append(i[1])
        return ans
