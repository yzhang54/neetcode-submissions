class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current = matrix[i][j]
                top = self.prefix[i-1][j] if i > 0 else 0
                left = self.prefix[i][j-1] if j > 0 else 0
                overlap = self.prefix[i-1][j-1] if i > 0 and j > 0 else 0

                self.prefix[i][j] += current + top + left - overlap
    # 0,0 1,1
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.prefix[row1-1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1-1] if col1 > 0 else 0
        overlap = self.prefix[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0
        res = self.prefix[row2][col2] - top - left + overlap

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)