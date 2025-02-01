class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r, c = len(img), len(img[0])
        ans = [[0]*c for _ in range(r)]
        fr = [1, 1, 0, -1, -1, -1, 0, 1]
        fc = [0, 1, 1, 1, 0, -1, -1, -1]
        for i in range(r):
            for j in range(c):
                sum, cnt = img[i][j], 1
                for k in range(8):
                    x = i+fr[k]
                    y = j+fc[k]
                    if(x >= 0 and x < r and y >= 0 and y < c):
                        sum += img[x][y]
                        cnt += 1
                print(sum, cnt)    
                ans[i][j] = sum//cnt
        return ans
