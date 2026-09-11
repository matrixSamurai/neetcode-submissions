class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Soltution 1 - Brute force - O(n^2)

        # for index, num in enumerate(nums):
        #     for num2 in nums[index+1:]:
        #         if num == num2:
        #             return True
        
        # return False

    

        # Solution 2
        # Sort the array - and then check for the duplicate
        # Time - O(nlogn), Space - O(1)

        # nums.sort()

        # if len(nums) > 0:
        #     prevNum = nums[0]

        # for num in nums[1:]:
        #     if prevNum == num:
        #         return True
        #     prevNum = num

        # return False



        # Solution 3
        # Create a map - Time complexity - O(n), Space Complexity - O(n)

        # duplicateMap = {}

        # for num in nums:
        #     if num in duplicateMap:
        #         return True
        #     else:
        #         duplicateMap[num] = 1
        
        # return False


        # Soltuion 4 - Create the hashset

        seenSet = set()

        for num in nums:
            if num in seenSet:
                return True
            seenSet.add(num)
        
        return False




       


        