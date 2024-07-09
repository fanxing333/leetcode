from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        for num in nums:
            for i in range(len(res)):
                res.append(res[i] + [num])
            res.append([num])

        res.append([])

        return res


if __name__ == "__main__":
    input = [1,2,3]

    s = Solution()
    print(s.subsets(input))
