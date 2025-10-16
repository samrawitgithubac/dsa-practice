class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=1
        maxss=0
        if  len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count+=1
            else:
                maxss=max(maxss,count)
                count=1
            if  len(nums)%2==1:
                if  count>=(len(nums)/2)+1:
                    return nums[i]
            else:
                if  count>=len(nums)/2:
                    return nums[i]
               

            
           
          
                
            
        

            


      
