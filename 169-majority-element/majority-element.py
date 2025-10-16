class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        
        for i in range(len(nums)):
            if count==0:
                count=1
                el=nums[i]
            elif nums[i]==el:
                count+=1
            else:
                count-=1
        return el
           
          
                
            
        

            


      
