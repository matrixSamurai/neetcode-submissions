class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        minGloblaRate = right

        while left <= right:
            rate = (left + right) // 2

            hoursConsume = 0

            for pile in piles:
                if pile % rate == 0:
                    hoursConsume += pile // rate
                else:
                    hoursConsume += (pile // rate) + 1

            if hoursConsume <= h:
                if rate < minGloblaRate:
                    minGloblaRate = rate
                right = rate -1
            else:
                left = rate + 1

        
        return minGloblaRate



        
       