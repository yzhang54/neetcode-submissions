class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        events = []
        for start,end, profit in zip(startTime, endTime, profit):
            events.append([start,end, profit])
        events.sort()

        print(events)
        memo = defaultdict(int) # index: profit
        def dfs(index):
            # base
            if index >= len(events):
                return 0
            if index in memo:
                return memo[index]

            curProfit = events[index][2]
            # explore next choices
            for nextIndex in range(index+1, len(events)):
                # overlap: we skip current
                if events[index][1] > events[nextIndex][0]:
                    curProfit = max(curProfit, dfs(nextIndex))
                # non-overlap
                else:
                    curProfit = max(curProfit, dfs(nextIndex) + events[index][2])

            memo[index] = curProfit
            return curProfit

        dfs(0)
        print(memo)
        return memo[0]
                