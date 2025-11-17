from math import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[comb(rowIndex,j) for  j in range(rowIndex+1)]
        return row 
       

        