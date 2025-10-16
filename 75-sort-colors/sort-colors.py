class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low=0
        high=len(nums)-1
        mid=0
        while low<=high and mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            #print(nums)
            elif  nums[mid]==1:
                mid+=1  
            #print(nums)
            
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums

       

           
