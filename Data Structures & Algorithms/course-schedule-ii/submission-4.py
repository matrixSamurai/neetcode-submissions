## In this solution, the code is sma eas the to detect the cycle, but we also want to check the correct order of completing the course, the good solution can after the node is fully explored, add it to the topological sort array, then then you have to reverse the array becuase the pre requisite nodes are explored fully first which are at the end of the array

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

#         state = [0] * numCourses
#         topo_order = []

#         ## Building the adjacency List
#         adj = {i : [] for i in range(numCourses)}
#         for u, v in prerequisites:
#             adj[v].append(u)
        

#         def hasCycle(node):

#             # print("The node is")
#             # print(node)

#             ## Base cases
            
#             if state[node] == 1:
#                 return True
            
#             if state[node] == 2:
#                 return False

#             ## work
#             state[node] = 1

#             ## Recursion Calls

#             for neighbor in adj[node]:
#                 if hasCycle(neighbor):
#                     return True
            
#             state[node] = 2

#             topo_order.append(node)

#             # print("The topo order is ")
#             # print(topo_order)

#             return False


#         for i in range(numCourses):
#             if state[i] == 0 and hasCycle(i):
#                 return []
        
#         return topo_order[::-1]


## Kahn's algorithm  Implementation

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        topo_order = []
        queue = deque()
        indegree = [0] * numCourses
        visit = set()

        adj = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        

        def kahns():

            while queue:

                node = queue.popleft()
                topo_order.append(node)

                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)


        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        kahns()

        if len(topo_order) != numCourses:
            return []
        
        return topo_order






        