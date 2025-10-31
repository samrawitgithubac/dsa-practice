class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ans=[]
        col=[0]*len(matrix[0])
        row=[0]*len(matrix)
        for  i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    col[j]=1
                    row[i]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (row[i])or(col[j])==1:
                    matrix[i][j]=0
        return matrix
                



               
        
        
        


