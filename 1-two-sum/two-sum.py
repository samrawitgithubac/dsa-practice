class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        for i in range(len(nums)):
            sums=nums[i]
            for j in range(i+1,len(nums)):
                sums+=nums[j]
                if sums==target:
                    return [i,j]
                else:
                    sums-=nums[j]
        





        
        


        