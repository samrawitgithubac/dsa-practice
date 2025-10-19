class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[0]*len(nums)
        postiveindex=0
        negativeindex=1
        for  i in range(len(nums)):
            if nums[i]<0:
                arr[negativeindex]=nums[i]
                negativeindex+=2
            
            else:
                arr[postiveindex]=nums[i]
                postiveindex+=2
        return arr

