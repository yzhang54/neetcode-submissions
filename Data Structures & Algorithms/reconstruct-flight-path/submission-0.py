class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list) # src:[des1, des2]

        for src, des in tickets:
            adjList[src].append(des)

        for src in adjList:
            adjList[src].sort(reverse=True)
            
        self.res = []
        def dfs(src):

            while adjList[src]:
                des = adjList[src].pop()
                dfs(des)

            self.res.append(src)

        dfs("JFK")
        self.res.reverse()

        return self.res


