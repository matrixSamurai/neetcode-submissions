class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        #Algorithm

        # 1. Create the minheap, with all the nodes with the value as 
        # infinity except for the source, which is 0
        # 2. Pick the element from the minheap, and update all it's neighbors in the minheap, and remove that picked element 
        # Now keep picking the min element from heap until the heap is
        # empty and keep on doing the step 2

        shortest = { i : -1 for i in range(n)}

        ## Creating the adjacency list to represent the graph
        adj = {i : [] for i in range(n)}
        for u, v, w in edges:
            adj[u].append((v, w))
        
        minHeap = []
        minHeap.append((0, src))

        while minHeap:

            w1, n1 = heapq.heappop(minHeap)

            ## THis will handle the override of the node, becuase it's greedy, if it's already been set, then it's the minimum possible
            if shortest[n1] != -1:
                continue
            
            shortest[n1] = w1

            for nei, w2 in adj[n1]:
                heapq.heappush(minHeap, (w1 + w2, nei))
        

        return shortest




        



        
