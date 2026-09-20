class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        state = [0] * numCourses
        topo_order = []

        ## Building the adjacency List
        adj = {i : [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[v].append(u)
        

        def hasCycle(node):

            # print("The node is")
            # print(node)

            ## Base cases
            
            if state[node] == 1:
                return True
            
            if state[node] == 2:
                return False

            ## work
            state[node] = 1

            ## Recursion Calls

            for neighbor in adj[node]:
                if hasCycle(neighbor):
                    return True
            
            state[node] = 2

            topo_order.append(node)

            # print("The topo order is ")
            # print(topo_order)

            return False


        for i in range(numCourses):
            if state[i] == 0 and hasCycle(i):
                return []
        
        return topo_order[::-1]



        