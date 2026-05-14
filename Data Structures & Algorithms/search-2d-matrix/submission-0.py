class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if target == matrix[i][j]:
                    return True

        return False
