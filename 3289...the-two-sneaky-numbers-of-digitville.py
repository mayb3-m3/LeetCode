class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        st = set()
        ans = []
        for i in nums:
            if i in st:
                ans.append(i)
            st.add(i)
        sorted(ans)
        return ans
