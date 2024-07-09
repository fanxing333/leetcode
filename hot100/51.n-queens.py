from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        output = []

        available = [[0 for _ in range(n)] for _ in range(n)]

        def available_init(row, col):
            sub_available = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == row or j == col:
                        sub_available[i][j] = 1
            
            for i in range(1, row+1):
                if col - i >= 0:
                    sub_available[row-i][col-i] = 1

                if col + i < n:
                    sub_available[row-i][col+i] = 1

            for i in range(1, n-row):
                if col + i < n:
                    sub_available[row+i][col+i] = 1

                if col - i >= 0:
                    sub_available[row+i][col-i] = 1

            return sub_available
        
        def matrix_add(A, B):
            for i in range(n):
                for j in range(n):
                    A[i][j] += B[i][j]

        def matrix_minus(A, B):
            for i in range(n):
                for j in range(n):
                    A[i][j] -= B[i][j]


        def backtrace(first=0, available=available):
            # 成功退出
            if first == n:
                res.append(output[:])

            # 如果 Queen 没有填满，但棋盘上没有位置填了则回溯
            if all(value > 0 for row in available for value in row):
                return
            
            for i in range(first, first+1):
                for j in range(n):
                    if available[i][j] == 0:
                        # output append
                        output.append("".join(["Q" if q == j else "." for q in range(n)]))
                        # available update
                        sub_available = available_init(i, j)
                        matrix_add(available, sub_available)

                        backtrace(first+1, available)

                        # backtrace
                        output.pop()
                        matrix_minus(available, sub_available)

            
        backtrace()

        return res

if __name__ == "__main__":
    input = 2

    s = Solution()
    print(s.solveNQueens(input))
