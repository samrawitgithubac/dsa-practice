class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s=""
        if n==0 or n==1:
            return True
        while n>0:
            a=n%2
            s+=str(a)
            n=n//2
        print(s)
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                return False
        else:
            return True
        
