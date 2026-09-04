class Solution:

    ## This is the most efficient solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []

        for index,num in enumerate(nums):

            if index > 0 and nums[index] == nums[index-1]:
                continue

            target = -1 * num

            left = index + 1
            right = len(nums)-1



            while left < right:

                sumTwo = nums[left] + nums[right]

                if sumTwo < target:
                    left += 1
                elif sumTwo > target:
                    right -= 1
                else:
                    result.append([nums[index],nums[left], nums[right]])

                    ## THis step is imp, as we move the pointers when 
                    ## we found the result, so we can find any more solutions if there
                    left += 1
                    right -= 1

                    ## Now, lets suppose, [-2,0,0,2,2], here if first -2 is selected
                    ## then next solution is [0,2], and then left and right are moved
                    ## and the next solution also becomes [0,2], we need to avoid, 
                    ## so we move the left pointer or right, till it's not same
                    while nums[right] == nums[right + 1] and left < right:
                       right -= 1

            
        
        return result

