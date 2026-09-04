class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for index, num in enumerate(numbers):
            remaining = target - num
         
            left = index + 1
            right = len(numbers) - 1
            ans = [0]
            
            while left <= right:
                mid = (left + right) // 2
        
                if numbers[mid] == remaining:
                    ans = [index+1, mid+1]
                    break
                elif numbers[mid] < remaining:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if ans != [0]:
                return ans

        return [0]


       

        