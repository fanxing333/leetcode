from typing import List

class Solution:
    """
    dp[i][j] 表示为到 text1[i] 和 text2[j] 为止的最长公共子序列的长度
    dp[i][j] = dp[i - 1][j - 1] + 1, text1[i] == text2[j]
    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]), otherwise
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, m):
            if dp[i - 1][0] == 1 or text1[i] == text2[0]:
                dp[i][0] = 1
        for i in range(1, n):
            if dp[0][i - 1] == 1 or text1[0] == text2[i]:
                dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

        return dp[m - 1][n - 1]

if __name__ == "__main__":
    input = "abcde"
    text2 = "ace" 

    s = Solution()
    print(s.longestCommonSubsequence(input, text2))
