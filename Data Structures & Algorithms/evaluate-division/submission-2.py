class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        mapping = defaultdict(list) # {a:[(b,val)]}

        for i in range(len(values)):
            first = equations[i][0]
            second = equations[i][1]

            mapping[first].append((second,values[i]))
            mapping[second].append((first,1/values[i]))

        def bfs(first, second):
            q = deque()
            visited = set()
            for nextSecond, nextVal in mapping[first]:
                q.append([nextSecond, nextVal]) 
                visited.add(nextSecond)

            while q:
                curFirst, curVal = q.popleft()

                if curFirst == second:
                    return curVal
                for nextSecond, nextVal in mapping[curFirst]:
                    
                    if nextSecond in visited:
                        continue
                    q.append([nextSecond, curVal*nextVal])
                    visited.add(nextSecond)
                
            return float(-1)


        res = []
        for first, second in queries:
            if first not in mapping or second not in mapping:
                res.append(float(-1))
            elif first == second:
                res.append(float(1)/1)
            else:
                res.append(bfs(first, second))

        return res
