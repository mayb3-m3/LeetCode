class Solution:
    def minimumSum(self, num: int) -> int:
        arr = list(str(num))
        arr = sorted(arr)
        arr[1], arr[2] = arr[2], arr[1]
        return int(''.join(arr[0:2])) + int(''.join(arr[2:]))
