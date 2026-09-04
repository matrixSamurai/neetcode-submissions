class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map1 = {}

        for char in s:
            if char in map1:
                map1[char] = map1[char]+1;
            else:
                map1[char] = 1
        
        for char in t:
            if char in map1 and map1[char] > 0:
                map1[char] = map1[char] - 1
            else:
                return False

        return True
                
        