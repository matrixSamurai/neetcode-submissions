class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## Brute force - two loops , time - O(n^2)

        ## HashMap

        seenMap = {}

        for index,num in enumerate(nums):
            seenMap[num] = index
        
        for index,num in enumerate(nums):
            searchNum = target - num
            if searchNum in seenMap and index != seenMap[searchNum]:
                if index < seenMap[searchNum]:
                    return [index, seenMap[searchNum]]
                else:
                    return  [seenMap[searchNum], index]
            


        