class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        numss=Counter(nums)
        for num in numss:
            if numss[num]==(len(nums)/2):
                return num
        
        