class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        ## THis is the classic Dijkstra's problem

        ## Creating the graph
        adj = {i : [] for i in range(1, n+1)}
        for u, v, t in times:
            adj[u].append((v, t))
        


        minTime = {i : -1 for i in range(1, n+1)}
        minHeap = [(0,k)]

        while minHeap:

            w1, n1 = heapq.heappop(minHeap)

            if minTime[n1] != -1:
                continue
            
            minTime[n1] = w1

            for n2, w2 in adj[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))

        
        maxVal = -1
        for time in minTime.values():
            if time == -1:
                return -1
            if maxVal < time:
                maxVal = time
            
            
        
        return maxVal
        