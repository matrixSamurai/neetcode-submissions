class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ## If we xor the each of the number from 0 to n and 
        ## then xor it with all the elements of array, the 
        ## result will be the missing number

        res= len(nums)

        for index, num in enumerate(nums):

            res = res ^ index ^ num
        
        return res
