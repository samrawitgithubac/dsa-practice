from collections import  Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_counters=Counter(nums)
        
        res=[]
        for i in  nums_counters:
            if nums_counters[i]>len(nums)/3:
                res.append(i)
        return res

               


            