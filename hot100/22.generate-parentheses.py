from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrace(first=0, output="", debt=0):
            if first == n:
                while debt > 0:
                    output += ")"
                    debt -= 1
                res.append(output)
                return

            if debt > 0:
                backtrace(first, output+")", debt-1)
            backtrace(first+1, output+"(", debt+1)
                    
        backtrace()
        return res

if __name__ == "__main__":
    input = 3

    s = Solution()
    print(s.generateParenthesis(input))
