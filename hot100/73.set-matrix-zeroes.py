from typing import List

class Solution:
    """
    按常规方式遍历矩阵
    同时，如果某元素左边的是 0 或上面的是 0，则将其置 0
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0

if __name__ == "__main__":
    input = [[1,1,1],[1,0,1],[1,1,1]]

    s = Solution()
    print(s.setZeroes(input))
    print(input)
