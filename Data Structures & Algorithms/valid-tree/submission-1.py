class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        ## A valid tree is a graph which doesn't have the cycle and all the edges are reachable from all the nodes
        # 1. No cycle
        # 2. All connected nodes

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n):

            if n == parent[n]:
                return n
            
            parent[n] = find(parent[n])

            return parent[n]
        
        def union(x, y):

            par_x = find(x)
            par_y = find(y)

            if par_x == par_y:
                return False
            
            if rank[par_x] > rank[par_y]:
                parent[par_y] = par_x
            elif rank[par_x] < rank[par_y]:
                parent[par_x] = par_y
            else:
                parent[par_y] = par_x
                rank[par_x] += 1

            return True
        
        for u, v in edges:
            if not union(u,v):
                return False
        
        count = 0
        for i in range(n):
            if parent[i] == i:
                count +=1
        
        if count > 1:
            return False
        
        return True
        


        

        


        