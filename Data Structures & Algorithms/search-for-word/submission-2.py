class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.directions = [[0, -1],[0, 1],[-1, 0],[1, 0]]

        def backtrack(tmp,i, j, index):
            if tmp == word:
                return True

            if len(tmp) >= len(word):
                return False

            if word[index] != board[i][j]:
                return False

            if board[i][j] == "#":
                return False
            curLetter = board[i][j]
            board[i][j] = "#"
            for dr,dc in self.directions:
                if not (dc+j in range(len(board[0]))):
                    continue
                if not (dr+i in range(len(board))):
                    continue
                if backtrack(tmp+board[dr+i][dc+j], dr+i, dc+j, index+1):
                    return True

            board[i][j] = curLetter

        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(board[row][col], row, col, 0):
                    return True

        return False
        # m*n*4^mn

            
