class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for index, num in enumerate(numbers):
            remaining = target - num
            print("new")
            left = index + 1
            right = len(numbers) - 1
            ans = [0]
            while left <= right:
                mid = (left + right) // 2
                print(remaining)
                print(num)
                print(numbers[mid])
                print(f"{left} : {right}")
                if numbers[mid] == remaining:
                    print(mid)
                    print(num)
                    ans = [index+1, mid+1]
                    break
                elif numbers[mid] < remaining:
                    print("I am here")
                    left = mid + 1
                    print(f"I am {left}")

                else:
                    right = mid - 1
            
            if ans != [0]:
                return ans

        return [0]


       

        