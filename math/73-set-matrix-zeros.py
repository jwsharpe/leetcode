class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        def zeroColRow(row,col):
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == row or c == col) and matrix[r][c] != None:
                        matrix[r][c] = 0


        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][c] = None


        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == None:
                    zeroColRow(r,c)
                    matrix[r][c] = 0
