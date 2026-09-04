class Solution:
    def topKFrequentHashMap(self, nums: List[int], k: int) -> List[int]:

        map1 = {}

        for num in nums:
            if num in map1:
                map1[num] += 1
            else:
                map1[num] = 1
        
        sorted_map = dict(sorted(map1.items(), key=lambda item: item[1], reverse=True))

        resultList = []
        for index, item in enumerate(sorted_map):
            if index < k:
                resultList.append(item)

        return resultList

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}

        for num in nums:
            # Use this method to default the value to 0, if the key is not present
            # This removes the need for handling of condition where the 
            # key is not present, map1.get(num,0), this phrase defaults it to 0 if not there
            map1[num] = 1 + map1.get(num,0)

        heap = []
        for num in map1.keys():
            # This is the imp step, we ar epushing the tuple in the sorting
            # So, in the tuple, the first element is considered first for comparison
            # and then the rest of the elements are considered
            heapq.heappush(heap, (map1[num], num))
            if len(heap) >k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

           








        