class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixArr = [0] * len(nums)
        prefixProduct = 1

        for index, num in enumerate(nums):
            prefixArr[index] = prefixProduct
            prefixProduct *= num

        print(prefixArr)

        result = [0] * len(nums)

        suffixProduct = 1

        # Thing to learn here is the how to traverse the list backwards
        for index in range(len(nums)-1, -1, -1):
            result[index] = suffixProduct * prefixArr[index]
            suffixProduct *= nums[index]

        return result

        