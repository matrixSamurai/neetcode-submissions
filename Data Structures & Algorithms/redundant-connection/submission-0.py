class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 1)]

        rank = [1] * (len(edges) + 1)

        def findParent(n):

            if n == parent[n]:
                return n
            
            parent[n] = findParent(parent[n])
            return parent[n]
        

        def isRedundant(x, y):

            par_x = findParent(x)
            par_y = findParent(y)

            if par_x == par_y:
                return True
            
            if rank[par_x] > rank[par_y]:
                parent[par_y] = par_x
            elif rank[par_x] < rank[par_y]:
                parent[par_x] = par_y
            else:
                parent[par_x] = par_y
                rank[par_y] += 1
            
            return False
        

        for u, v in edges:
            if isRedundant(u,v):
                return [u,v]










        