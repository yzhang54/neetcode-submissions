class TimeMap:

    def __init__(self):
        self.keyToVal = defaultdict(list) # key: {[val, time], [val2, time2]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToVal[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        #TTTTFFF
        curList = self.keyToVal[key]

        if len(curList) == 0:
            return ""

        left, right = 0, len(curList) - 1
        while left <= right:
            mid = (left+right)//2

            if curList[mid][1] <= timestamp: # this is true 
                left = mid + 1
            else:
                right = mid - 1
        if right == -1:
            return ""
        return curList[right][0]
