class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arry1=[]
        arry2=[]
       
        i=0
        for i in range(len(nums)):
            if nums[i]>0:
                arry1.append(nums[i])
            else:
                arry2.append(nums[i])
        j=0
        for i in range(len(arry1)):
            if j%2==0:
                nums[j]=arry1[i]
                j+=2
        j=1
        for i in range(len(arry2)):
            if j%2==1:
                nums[j]=arry2[i]
                j+=2
        
            
        return nums
               
               
          


        
        

            
            
