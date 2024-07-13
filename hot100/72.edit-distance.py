from typing import List

class Solution:    
    """
    dp[i][j] 表示 word1[:i+1] 到 word2[:j+1] 的最短距离
    
    """
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0 if word1[0] == word2[0] else 1
        for i in range(1, m):
            if word1[i] == word2[0]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n):
            if word1[0] == word2[i]:
                dp[0][i] = i
            else:
                dp[0][i] = dp[0][i - 1] + 1

        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        print(dp)
        return dp[m - 1][n - 1]
        


if __name__ == "__main__":
    input = "horse"
    word2 = "ros"

    input = "intention"
    word2 = "execution"

    s = Solution()
    print(s.minDistance(input, word2))
