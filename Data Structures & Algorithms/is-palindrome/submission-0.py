class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        snew = ''.join(c.lower() for c in s if c.isalnum())


        for i in range(0,int(len(snew)/2)):
            if snew[i] != snew[len(snew)-1-i]:
                return False
        
        return True


        