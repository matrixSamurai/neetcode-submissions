class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:


        answer = []
        maps = {}
        stack = []

        for i in range(len(nums2)):

            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                maps[nums2[index]] = nums2[i]
            
            stack.append(i)

        print(maps)
        
        for i in range(len(nums1)):
            answer.append(maps.get(nums1[i], -1))
        
        return answer


        



        