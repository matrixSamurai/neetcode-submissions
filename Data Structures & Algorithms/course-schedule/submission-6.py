## This is the classic proble of detecting the cycle in the graph
## and the standar way to detect the cycle in the graph is to maintain the 
## 3 state state array of the nodes, in which we keep the states as the following
## 1. Unvisited 2. Processing 3. Processed fully
## The idea is that if the node is in the processing state and we reach that node again it, means that in the same branch and the stack of the dfs call we have reached that same node again and hence the cycle appears.
## And if the node fully processed which means all of it's neighbors are processed without detecting the cycle, there is no cycle in that recursive stack

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        ## Declaring the empty state array 
        state = [0] * numCourses

        ## Creating the adjaceny list of the map
        adj = {i : [] for i in range(numCourses)} 
        ## Adding all the edges in the map
        for u, v in prerequisites:
            adj[u].append(v)

        
        def has_cycle(node):

            ## BAse cases
            if state[node] == 1:
                return True
            
            if state[node] == 2:
                return False

            state[node] = 1

            for neighbor in adj[node]:
                if has_cycle(neighbor):
                    return True
            
            state[node] = 2
            return False

        

        for i in range(numCourses):
            if state[i] == 0 and has_cycle(i):
                return False
        
        return True
        