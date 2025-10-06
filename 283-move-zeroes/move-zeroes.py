class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]== 0:
                nums.pop(i)
                count+=1
        for i in range(count):
            nums.append(0)

        return nums
                
       