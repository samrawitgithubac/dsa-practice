class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        lastbit=n&1
        n>>=1
        while n>0:
            currentbit=n&1
            if currentbit==lastbit:
                return False
            lastbit=currentbit
            n>>=1
        return True
       
        
        