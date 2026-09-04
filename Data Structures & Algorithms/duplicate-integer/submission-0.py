class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = {};
        for num in nums:
            if map1.get(num):
                return True
            else:
                map1[num] = 1
        
        return False
        