class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

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






        