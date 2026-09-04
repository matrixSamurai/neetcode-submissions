class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Python automatically does not have the maxheap class, so we have
        # to use the min heap intelligently
        pq =[]

        for num in stones:
            heapq.heappush(pq, num * -1)
        
        while len(pq) > 1:
            x = heapq.heappop(pq) * -1
            y = heapq.heappop(pq) * -1

            if x != y:
                heapq.heappush(pq, (x-y) * -1)
        
        if len(pq) > 0:
            return heapq.heappop(pq) * -1
        else:
            return 0





