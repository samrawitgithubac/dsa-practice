class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxss=float('-inf')
        count=0
        c=0
        for  num in nums:
            if num<0:
                c+=1
        if c==len(nums):
            return max(nums)
        if len(nums)==1:
            return  nums[0]
        for num in nums:
            count+=num
            if count<0:
                count=0
            maxss=max(maxss,count)
        return maxss
