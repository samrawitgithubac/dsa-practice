class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for  i in range(len(nums)):
            s=target-nums[i]
            if  s in nums and nums.index(s)!=i:
                return [i, nums.index(s)]



      
       






        
        


        