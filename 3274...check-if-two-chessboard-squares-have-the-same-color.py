class Solution:
   def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
      d1 = abs(ord(coordinate1[0]) - ord(coordinate2[0]))
      d2 = abs(int(coordinate1[1]) - int(coordinate2[1]))
      if (d1 + d2) % 2 == 0:
         return True
      else:
         return False
