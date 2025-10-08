class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap1={'1':0,'0':0}
        ans=[]
        numss=set(nums)
        if len(numss)==1 and numss==0:
            return 0
        
        for num in nums:
            if  num==1:
                hashmap1['1']+=1
            else:
                hashmap1['0']+=1
                ans.append(hashmap1['1'])
                hashmap1['1']=0
        ans.append(hashmap1['1'])
        return max(ans)

                
               


            
        
           
        
            

            


        