class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        ## Here we have to only compare the right to the mid
        ## if the mid > right ; then the answer is in the right section

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]


        