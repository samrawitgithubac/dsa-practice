class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize both current and global maximum to the first element
        current_sum = max_sum = nums[0]
        
        # Iterate from the second element
        for num in nums[1:]:
            # Either extend the current subarray or start a new one
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
