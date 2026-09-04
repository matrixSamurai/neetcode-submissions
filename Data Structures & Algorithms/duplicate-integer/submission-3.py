class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Solution 1
        # Create a map - Time complexity - O(n), Space Complexity - O(n)

        # duplicateMap = {}

        # for num in nums:
        #     if num in duplicateMap:
        #         return True
        #     else:
        #         duplicateMap[num] = 1
        
        # return False

        # Solution 2
        # Sort the array - and then check for the duplicate
        # Time - O(nlogn), Space - O(1)

        nums.sort()

        if len(nums) > 0:
            prevNum = nums[0]


        for num in nums[1:]:
            if prevNum == num:
                return True
            prevNum = num

        return False

       


        