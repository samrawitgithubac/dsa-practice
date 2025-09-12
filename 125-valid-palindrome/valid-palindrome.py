import re
class Solution(object):
    def isPalindrome(self, s):
        st=[]
        for i in s:
            if i.isalnum():
                st.append(i.lower())
        n=len(st)
       
        def  check(i,n):
            if i>=n/2:
                return True
            if st[i]!=st[n-i-1]:
                return False
            return  check(i+1,n)
        return  check(0,n)




   
    
        

            
            

            

       
