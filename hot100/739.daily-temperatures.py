from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = i - idx
                stack.append(i)

        return res

if __name__ == "__main__":
    input = [73,74,75,71,69,72,76,73]

    s = Solution()
    print(s.dailyTemperatures(input))
