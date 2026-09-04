class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxContain = 0;

        for index, bar1 in enumerate(heights):
            for index2 in range(index + 1, len(heights)):
                contain = (index2-index) * min(heights[index],heights[index2])
                if contain > maxContain:
                    maxContain = contain
        
        return maxContain
        
        