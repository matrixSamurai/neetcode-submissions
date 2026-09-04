class Solution:
    def trapEfficient(self, height: List[int]) -> int:

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

    # THis below is the inefficient solution
    def trap(self, height: List[int]) -> int:

        result = 0

        for index, num in enumerate(height):
            maxLeft = height[index]
            maxRight = height[index]
            for i in range(index -1, -1, -1):
                if height[i] > maxLeft:
                    maxLeft = height[i]
            for i in range(index +1, len(height)):
                if height[i] > maxRight :
                    maxRight = height[i]
            
            result += max(0,min(maxRight, maxLeft) - height[index])

        return result





        