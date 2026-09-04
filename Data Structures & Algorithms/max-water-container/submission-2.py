class Solution:
    def maxAreaInefficient(self, heights: List[int]) -> int:

        maxContain = 0;

        for index, bar1 in enumerate(heights):
            for index2 in range(index + 1, len(heights)):
                contain = (index2-index) * min(heights[index],heights[index2])
                if contain > maxContain:
                    maxContain = contain
        
        return maxContain
        
    # Efficient Soltuion
    def maxArea(self, heights: List[int]) -> int:

        maxVal = 0
        left = 0
        right = len(heights)-1

        while left < right:
            volume = (right - left) * min(heights[right], heights[left])
            if volume > maxVal:
                maxVal = volume
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        
        return maxVal
            



        