class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.numToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.numToIndex:
            return False

        self.nums.append(val)
        self.numToIndex[val] = len(self.nums) - 1
        

    def remove(self, val: int) -> bool:
        if val not in self.numToIndex:
            return False

        removeIndex = self.numToIndex[val]
        lastIndex = len(self.nums) - 1
        removedVal = val
        lastVal = self.nums[-1]
        print("self.numToIndex", self.numToIndex)
        print("self.nums", self.nums)
        print("removeIndex", removeIndex)
        print("lastIndex", lastIndex)
        self.nums[removeIndex], self.nums[lastIndex] = self.nums[lastIndex], self.nums[removeIndex]
        self.numToIndex[removedVal], self.numToIndex[lastVal] = self.numToIndex[lastVal], self.numToIndex[removedVal]
        print("self.numToIndex", self.numToIndex)
        print("self.nums", self.nums)

        self.nums.remove(self.nums[lastIndex])
        self.numToIndex.pop(val)


    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()