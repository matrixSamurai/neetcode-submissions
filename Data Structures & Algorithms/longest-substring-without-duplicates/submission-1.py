class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ## Sliding window problem

        sptr = 0
        seenSet = set()
        result = 0
        maxResult = 0

        for char in s:
            if char in seenSet:
                while char in seenSet:
                    result -= 1
                    print(seenSet)
                    print(char)
                    print(s[sptr])
                    seenSet.remove(s[sptr])
                    sptr += 1
            
            
            seenSet.add(char)
            result +=1
            if result > maxResult:
                maxResult = result

        
        return maxResult






        