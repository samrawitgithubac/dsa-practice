class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[[1],[1,1]]
       
        if numRows==1:
            return [[1]]
        if numRows==2:
            return ans
        for i  in range(2,numRows):
            col=[1]
            for j  in range(1,i):
                s=ans[i-1][j-1]+ans[i-1][j]
                col.append(s)
            col.append(1)
            ans.append(col)
        return ans 
               

           



        