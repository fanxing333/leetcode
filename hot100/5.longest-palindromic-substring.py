from typing import List

class Solution:
    """
    回文串的子串一定是回文串，所以有
    dp[i][j] 表示 s[i: j + 1] 是回文串
    dp[i][j] = dp[i + 1][j - 1] & s[i] == s[j], i < j - 1
    dp[i][j] = s[i] == s[j], i = j - 1
    dp[i][j] = True, i = j
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True if i==j else False for j in range(n)] for i in range(n)]

        max_length = 1
        max_palindrome = s[0]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if i + 1 < j:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j]

                if dp[i][j] and max_length < j - i + 1:
                    max_length = j - i + 1
                    max_palindrome = s[i: j+1]
        
        return max_palindrome

if __name__ == "__main__":
    input = "babad"

    s = Solution()
    print(s.longestPalindrome(input))
