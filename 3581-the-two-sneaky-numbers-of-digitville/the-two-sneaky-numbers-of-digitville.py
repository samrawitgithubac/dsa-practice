class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        hashmap={}
        ans=[]
        for  i in range(len(nums)):
            if nums[i] in  hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        for  i in  hashmap:
            if hashmap[i]==2:
                ans.append(i)
        return ans


            

        

        