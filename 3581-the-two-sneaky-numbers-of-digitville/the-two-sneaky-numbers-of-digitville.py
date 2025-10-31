class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans=[]
        for  i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                ans.append(nums[i])
        return ans


            

        

        