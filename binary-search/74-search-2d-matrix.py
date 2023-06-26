class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = (l + r) // 2
            row = m // ROWS
            col = m % COLS

            if target == matrix[row][col]:
                return True
                
            if target < matrix[row][col]:
                r = m - 1
            else:
                l = m + 1
        return False
