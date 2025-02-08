class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        st, n, one = set(), len(grid), 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] in st:
                    one = grid[i][j]
                else:
                    st.add(grid[i][j])
        for i in range(n*n):
            if i+1 not in st:
                return [one, i+1]
