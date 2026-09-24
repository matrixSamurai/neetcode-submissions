class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:


        maxSeenTillNow = 0
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        ROW, COL = len(grid), len(grid[0])


        while minHeap:

            val, r, c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue
            
            visit.add((r,c))

            if r == ROW -1 and c == COL -1:
                return max(maxSeenTillNow, grid[r][c])

            if val > maxSeenTillNow:
                maxSeenTillNow = val
            

            for dr, dc in neighbors:
                tr = r + dr
                tc = c + dc

                if min(tr, tc) < 0 or tr >= ROW or tc >= COL:
                    continue

                heapq.heappush(minHeap, (grid[tr][tc], tr, tc))


            



            
            


        