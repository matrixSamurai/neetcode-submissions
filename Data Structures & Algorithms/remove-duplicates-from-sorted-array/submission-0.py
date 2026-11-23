class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ## Use the two pointer (read and write pointer) - (slow and fast)
        # slow for writing and fast for reading all elements in arr

        slow = 1

        for fast in range(1, len(nums)):

            if nums[slow - 1] != nums[fast]:

                nums[slow] = nums[fast]
                slow += 1
        
        return slow
    






        