class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1   # eliminate column
            else:
                r += 1   # eliminate row
        return False
