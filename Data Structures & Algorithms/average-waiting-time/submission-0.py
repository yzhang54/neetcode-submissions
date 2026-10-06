class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        curTime = customers[0][0]
        totalAvgTime = 0
        for i in range(len(customers)):
            # curTime = min(curTime, )

            if curTime < customers[i][0]:
                curTime = customers[i][0]
            duration = customers[i][1]
            arrival = customers[i][0]
            totalAvgTime += (curTime - arrival + duration)
            curTime += duration
            # print(curTime)

        print(totalAvgTime)
        return totalAvgTime/len(customers)

