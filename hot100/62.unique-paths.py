from typing import List

class Solution:
    """
    dp[i][j] 表示到 (i, j) 的所有路径
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n if i == 0 else [1] + [0] * (n - 1) for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

if __name__ == "__main__":
    input = 3
    n = 7

    s = Solution()
    print(s.uniquePaths(input, n))
