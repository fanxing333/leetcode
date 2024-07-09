from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        res.append([start, end])
        
        return res

if __name__ == "__main__":
    input = [[1,3],[2,6],[8,10],[15,18]]

    s = Solution()
    print(s.merge(input))
