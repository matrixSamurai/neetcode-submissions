class Solution:
    def trap(self, height: List[int]) -> int:

        leftmaxArray = [0] * len(height)
        leftmax = 0
        result = 0
        rightmax = 0


        for index, num in enumerate(height):
            leftmaxArray[index] = leftmax
            leftmax = max(leftmax, num)
        
        for index in range(len(height)-1 , -1, -1):
            # THis line is for calcualting the water, the water cannot be less than 0
            result += max(0, min(leftmaxArray[index],rightmax) - height[index])
            rightmax = max(rightmax, height[index])

        return result


        