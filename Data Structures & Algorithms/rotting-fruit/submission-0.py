class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source bfs: store all rotten fruits, we traverse layer by layer until all fruits are rotten. we also need to travser the grid one time at end to check -1 case. 

        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j, 0])
                    visited.add((i,j))

        res = 0
        while q:
            row, col, time = q.popleft()

            res = max(res, time)

            for dr, dc in [[0, -1],[0, 1], [1, 0], [-1, 0]]:
                nextR, nextC = row+dr, col+dc

                if nextR not in range(len(grid)) or nextC not in range(len(grid[0])):
                    continue

                if (nextR, nextC) in visited:
                    continue
                if grid[nextR][nextC] == 0 or grid[nextR][nextC] == 2:
                    continue

                if grid[nextR][nextC] == 1:
                    grid[nextR][nextC] = 2

                q.append([nextR, nextC, time+1])
                visited.add((nextR, nextC))

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        
        return res


                

