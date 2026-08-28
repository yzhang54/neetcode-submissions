class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        def dfs(row, col, zeros, visited): # we collect all positions for the cell "0", and the all "0" cell are conected
            if row not in range(len(board)) or col not in range(len(board[0])):
                return 
            if (row, col) in visited:
                return 
            if board[row][col] == "X":
                return 

            zeros.add((row, col))
            visited.add((row, col))
            dfs(row+1, col, zeros, visited)
            dfs(row-1, col, zeros, visited)
            dfs(row, col+1, zeros, visited)
            dfs(row, col-1, zeros, visited)


        self.res = set()
        # print(len(board))
        # print(len(board[0]))
        for i in range(len(board)):
            for j in range(len(board[0])):
                # print("i:" + str(i))
                # print("j:"+str(j))
                # print(board[i][j] == "O" and (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1))
                if board[i][j] == "O" and (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1):
                    zeros = set()
                    visited = set()
                    dfs(i, j, zeros, visited)
                    
                    print(self.res)
                    self.res = self.res | zeros

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in self.res:
                    board[i][j] = "X"

        