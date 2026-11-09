class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i,j, 0])
                    visited.add((i,j))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            r, c, dis = q.popleft()

            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if nextR not in range(len(grid)) or nextC not in range(len(grid[0])):
                    continue 
                if grid[nextR][nextC] == -1:
                    continue
                if (nextR, nextC) in visited:
                    continue 

                if grid[nextR][nextC] == 2147483647:
                    grid[nextR][nextC] = dis + 1
                q.append([nextR, nextC, dis+1])
                visited.add((nextR, nextC))

