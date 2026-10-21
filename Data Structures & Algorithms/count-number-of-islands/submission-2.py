class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(row, col):
            if grid[row][col] == "0":
                return 

            grid[row][col] = "0"

            for dr, dc in directions:
                nr, nc  = row + dr, col + dc

                if nr not in range(len(grid)) or nc not in range(len(grid[0])):
                    continue 
                dfs(nr, nc)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    print("test")
                    dfs(i,j)
                    res += 1
        print(grid)
        return res
