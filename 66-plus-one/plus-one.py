class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        res=[]
        for num in digits:
            s+=str(num)
        s=int(s)+1
        s=str(s)
        for num in s:
            res.append(int(num))
        return res
        
       
        
       

    

       