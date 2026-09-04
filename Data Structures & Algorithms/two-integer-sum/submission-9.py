class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## Solution 1 ; Brute force - two loops , time - O(n^2)

        ## Soltuion 2; HashMap - time - O(n), space - O(n)

        # seenMap = {}

        # for index,num in enumerate(nums):
        #     seenMap[num] = index
        
        # for index,num in enumerate(nums):
        #     searchNum = target - num
        #     if searchNum in seenMap and index != seenMap[searchNum]:
        #         if index < seenMap[searchNum]:
        #             return [index, seenMap[searchNum]]
        #         else:
        #             return  [seenMap[searchNum], index]

        # Soltuion 3 : Use the sorting
        # arr = []

        # for index,num in enumerate(nums):
        #     arr.append([num, index])
        
        # arr.sort()

        # endPointer = len(arr)-1
        # startPointer = 0

        # while(startPointer < endPointer):
        #     if target > arr[startPointer][0] + arr[endPointer][0]:
        #         print(arr[startPointer][0] + arr[endPointer][0])
        #         startPointer += 1
        #     elif target < arr[startPointer][0] + arr[endPointer][0]:
        #         print(arr[startPointer][0] + arr[endPointer][0])
        #         endPointer -= 1
        #     else:
        #         print(arr[startPointer][0] + arr[endPointer][0])
        #         return [arr[startPointer][1],arr[endPointer][1]]

        # return []

        # One pass hashmap 

        searchMap = {}

        for index, num in enumerate(nums):
            if target - num in searchMap:
                return [min(index, searchMap[target - num] ), max(index, searchMap[target - num])]
            else:
                searchMap[num] = index
        
        
        

       

            


        