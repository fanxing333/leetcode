from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        res = [[1], [1, 1]]
        for row in range(2, numRows):
            res.append([1] * (row + 1))
            for j in range(1, row):
                res[row][j] = res[row - 1][j - 1] + res[row - 1][j]

        return res

if __name__ == "__main__":
    input = 5

    s = Solution()
    print(s.generate(input))
