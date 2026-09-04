class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        map1 = set()
        left = 0
        right = 0
        result = 0

        while right < len(s):
            if s[right] in map1:
                map1.remove(s[left])
                left += 1
            else:
                map1.add(s[right])
                right += 1
                result = max(right - left, result)
                
        
        return result





        