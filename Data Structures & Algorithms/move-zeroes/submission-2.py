class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0

        for fast in range(1, len(nums)):

            if nums[slow] != 0:
                slow += 1
                continue

            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            
            
            
        