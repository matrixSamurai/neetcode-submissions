class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left < right:

            midRate = (left + right ) // 2

            reqHours = 0

            for i in range(len(piles)):
                reqHours += math.ceil( piles[i] / midRate)
               
            
            if reqHours > h:
                left = midRate + 1
            elif reqHours <= h:
                right = midRate
        
        return left
                


        