class Solution:
    def check(self, nums: List[int]) -> bool:
        x=0
        b=[0 for i in range(len(nums))]
        for  x in range(len(nums)):
            for i in range(len(nums)):
                b[i]=nums[(i+x)%(len(nums))]
          
            if sorted(nums)==b:
                return True
           
        return False


            
            
        