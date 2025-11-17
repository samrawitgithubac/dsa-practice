from math import comb
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(numRows):
            row=[comb(i,j) for  j in range(i+1)]
            ans.append(row)
        return ans

        