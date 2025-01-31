class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [""]*numRows
        index, change = 0, 1
        for ch in s:
            arr[index] += ch
            if index == numRows-1 and change == 1:
                index = max(index-1, 0)
                change = -1
            elif index == 0 and change == -1:
                index = min(index+1, numRows-1)
                change = 1
            else:
                index += change
        return "".join(arr)
