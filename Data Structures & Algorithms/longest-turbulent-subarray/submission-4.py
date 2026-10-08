class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        res = []
        maxRes = 0
        for i in range(len(arr)):
            # print("current index: ", i)
            # print(res)
            current = arr[i]
            if res and res[-1] == current:
                res = [current]
                continue
            if len(res) >= 2:
                prevOne = res[-2]
                prevTwo = res[-1]
                # prev pair is <
                if prevOne < prevTwo:
                    # print(prevTwo)
                    # print(current)
                    if prevTwo > current:
                        res.append(current)
                    elif current == prevTwo:
                        res = [current]
                    else:
                        res = [prevTwo, current]
                # prev pair is >
                elif prevOne > prevTwo:
                    # print(prevTwo)
                    # print(current)
                    if prevTwo < current:
                        res.append(current)
                    elif current == prevTwo:
                        res = [current]
                    else:
                        res = [prevTwo, current]
            else:
                res.append(arr[i])

            # print(res)
            maxRes = max(maxRes, len(res))

        return maxRes