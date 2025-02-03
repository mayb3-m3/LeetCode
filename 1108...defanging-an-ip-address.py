class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = list(address)
        for i in range(len(arr)):
            if arr[i] == '.':
                arr[i] = "[.]"
        return ''.join(arr)
