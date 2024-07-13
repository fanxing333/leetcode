from typing import List

class Solution:
    """
    栈
    假设一直有效，
    """
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    longest = max(longest, i - stack[-1])
                else:
                    stack.append(i)
                    

        return longest
    """
    为什么想到要用动态规划？
    即使这个动态规划要比栈复杂太多
    """
    def longestValidParentheses2(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 0
        stack = [0] * (len(s) + 1)

        for i in range(len(s)):
            if s[i] == "(":
                dp[i + 1] = dp[i] + 1
                stack[i + 1] = stack[i] + 1
            else:
                if stack[i] > 0:
                    dp[i + 1] = dp[i] + 1
                    stack[i + 1] = stack[i] - 1
                else:
                    dp[i + 1] = 0
                    stack[i + 1] = 0
            
        print(dp)
        print(stack)

        longest = 0
        for i in range(len(s)):
            if stack[i + 1] == 0:
                longest = max(longest, dp[i + 1])
        return longest

if __name__ == "__main__":
    input = ")()()))((((()))))(((((((())))))))))))))"
    input = "(()"

    s = Solution()
    print(s.longestValidParentheses(input))
