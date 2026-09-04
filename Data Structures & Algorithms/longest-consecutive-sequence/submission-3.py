class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        map1 = defaultdict(set)

        for num in nums:
            map1[num] = 1

        beginNum = 0
        length = 0
        longest = length

        for num in map1.keys():
            if num-1 not in map1:
                beginNum = num
                length = 1
            while beginNum + length in map1:
                length += 1
            
            longest = max(length, longest)
            
 
        return longest


        


          



        