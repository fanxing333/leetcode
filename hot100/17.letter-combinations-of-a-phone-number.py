from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        n = len(digits)
        if n == 0:
            return []
        
        def backtrace(first=0, output=""):
            if first == n:
                res.append(output)
                return
            
            choices = number_map[digits[first]].copy()
            for i in range(len(number_map[digits[first]])):
                char = choices.pop()
                output += char

                backtrace(first+1, output)

                output = output[:-1]
        
        backtrace()

        return res

if __name__ == "__main__":
    input = "4"

    s = Solution()
    print(s.letterCombinations(input))
