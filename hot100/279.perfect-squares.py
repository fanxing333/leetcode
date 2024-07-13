from typing import List
import math

class Solution:
    """
    维护一个 count[i] 数组
    count[i] 表示构成 i + 1 所需要的最少平方数
    """
    def numSquares(self, n: int) -> int:
        count = [10000] * n
        count[0] = 1

        for i in range(1, n):
            for j in range(1, 101):
                if j * j == i + 1:
                    count[i] = 1
                elif j * j < i + 1:
                    count[i] = min(count[i - j * j] + 1, count[i])
                else:
                    break

        return count[-1]

if __name__ == "__main__":
    input = 12

    s = Solution()
    print(s.numSquares(input))
