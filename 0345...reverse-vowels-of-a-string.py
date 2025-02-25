class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        idx = [i for i, ch in enumerate(s) if ch in vowels]
        n, lst = len(idx), list(s)
        for i in range(n//2):
            lst[idx[i]], lst[idx[n-1-i]] = lst[idx[n-1-i]], lst[idx[i]]
        return ''.join(lst)
