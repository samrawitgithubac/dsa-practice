class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap1={}
        for i,num  in enumerate(nums):
            s=target-num
            if s in hashmap1:
                return [i,hashmap1[s]]
            else:
                hashmap1[num]=i
        



      
       






        
        


        