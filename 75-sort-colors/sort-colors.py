class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countzero=0
        countone=0
        counttwo=0
        for i in range(len(nums)):
            if nums[i]==0:
                countzero+=1
            elif nums[i]==1:
                countone+=1
            else:
                counttwo+=1
        for i in range(countzero):
            nums[i]=0
        s=countone+countzero
        h=s+counttwo
        for  i in range(countzero,s):
            nums[i]=1
        for i in range(s,h):
            nums[i]=2
        return nums
       
       

           
