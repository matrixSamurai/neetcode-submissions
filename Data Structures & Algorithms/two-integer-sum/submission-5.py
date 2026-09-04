class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map1 = {}
        answer = []

        for index,num in enumerate(nums):
            map1[num] = index

        for index, num in enumerate(nums):
            if target-num in map1 and index != map1[target-num]:
                answer = [index, map1[target-num]]
                break
        
        answer.sort()
        return answer

            


        