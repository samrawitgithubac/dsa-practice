import re
class Solution(object):
    def isPalindrome(self, s):
        strs=[]
        for i in s:
            if  i.isalnum():
                strs.append(i.lower())
        
        if strs==strs[::-1]:
            return True
        else:
            return False
   
    
        

            
            

            

       
