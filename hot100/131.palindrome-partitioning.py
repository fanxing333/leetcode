from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        output = []
        n = len(s)

        # 检查字符串 s 是否是回文串
        def check_palindromic(s):
            if len(s) == 1:
                return True
            else:
                for i in range(len(s)//2):
                    if s[i] != s[len(s) - 1 - i]:
                        return False
                    
            return True

        def backtrace(first=0, p=""):
            if first == n:
                res.append(output[:])
            
            for i in range(first, n):
                if check_palindromic(p+s[i]):
                    output.append(p+s[i])

                    backtrace(i+1, p="")

                    output.pop()
                p += s[i]
                
        backtrace()

        return res

if __name__ == "__main__":
    input = "efe"

    s = Solution()
    print(s.partition(input))
