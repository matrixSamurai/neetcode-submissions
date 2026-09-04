class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                p = stack.pop()[1]
                result[p] = index - p
            
            stack.append((temp, index))
        
        while len(stack) > 0:
            p = stack.pop()[1]
            result[p] = 0
        
        return result



            


        
