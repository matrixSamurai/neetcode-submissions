class TimeMap:

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.keyStore:
            self.keyStore[key].append((timestamp, value))
        else:
            newList = [(timestamp, value)]
            self.keyStore[key] = newList
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.keyStore:
            return ""
        
        keyList = self.keyStore[key]
        left = 0
        right = len(keyList)

        while left < right:

            mid = (left + right ) // 2

            if keyList[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid 
        
        return keyList[left - 1][1] if left != 0 else ""
        
