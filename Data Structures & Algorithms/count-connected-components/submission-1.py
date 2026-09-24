## We can find the disjoint set union algorithm to find the connected components here

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        disconnectedComps = n

        parent = [i for i in range(n)]

        rank = [1] * n


        def findParent(n):

            if parent[n] == n:
                return n
            
            parent[n] = findParent(parent[n])
            return parent[n]
        

        def union(x, y):

            par_x = findParent(x)
            par_y = findParent(y)

            if par_x == par_y:
                return

            nonlocal disconnectedComps
            disconnectedComps -= 1

            if rank[par_x] > rank[par_y]:
                parent[par_y] = par_x
            elif rank[par_x] < rank[par_y]:
                parent[par_x] = par_y
            else:
                parent[par_x] = par_y
                rank[par_y] += 1
            

        for u, v in edges:
            union(u,v)
        
        return disconnectedComps
        


        