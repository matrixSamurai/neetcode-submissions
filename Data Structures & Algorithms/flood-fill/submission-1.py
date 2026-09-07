## DFS Solution
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


#         visit = set()
#         ROW, COL = len(image), len(image[0])

#         def dfs(r, c, oldColor, newColor):


#             if min(r,c)< 0 or r== ROW or c== COL or image[r][c] != oldColor or (r,c) in visit:
#                 return
            
#             image[r][c] = newColor
#             visit.add((r,c))

#             dfs(r-1,c, oldColor, newColor)
#             dfs(r+1,c, oldColor, newColor)
#             dfs(r,c+1, oldColor, newColor)
#             dfs(r,c-1, oldColor, newColor)

        
#         dfs(sr, sc, image[sr][sc], color)

#         return image
        

## BFS Solution
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        queue = deque()
        visit = set()
        neighbors = [(1,0), (-1,0), (0, 1), (0, -1)]
        origColor = image[sr][sc]
        queue.append((sr,sc))

        while queue:

            x, y = queue.popleft()

            if image[x][y] == origColor:
                image[x][y] = color

            for dx, dy in neighbors:
                tr = x + dx
                tc = y + dy

                if min(tr,tc) < 0 or tr == len(image) or tc == len(image[0]) or image[tr][tc] != origColor:
                    continue

                if (tr,tc) not in visit:
                    visit.add((tr,tc))
                    queue.append((tr,tc))
        
        return image

            










