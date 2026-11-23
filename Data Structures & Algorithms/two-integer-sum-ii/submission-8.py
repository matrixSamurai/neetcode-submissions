class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Using the 2 pointer solution here to solve
        # time complexity - O(n)

        left = 0
        right = len(numbers) -1

        while left < right:

            curr_sum = numbers[left] + numbers[right] 

            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [left+1, right+1]
        
        return []

        ## ANother solution can be to use the binary search to 
        ## to search the remaining sum for all the elements
        # The time complexity for this will - O(n * logn)
        

        ## Another bad solution can be O(n^2), using the two loops
        