from typing import List

class Solution:
    """
    把字符串划分成不同的片段，同一个字母只能出现在一个片段中
    从前往后遍历字符串，对于指针所指的 char，从后往前遍历直到它出现，下一次指针在它的右边
    对于子串里的所有 char，都应该不停的从后往前遍历，构建出一个最大的不重复子串

    因为 s 中只有小写字母，所以维护一个字典，记录每个 char 最后出现的 index，最差时间复杂度 O(n)
    再从前往后遍历，不停扩大子串，记录 right 的最大值
    """
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        n =  len(s)
        last_appear_index = {}
        for i in range(n-1, -1, -1):
            if s[i] not in last_appear_index.keys():
                last_appear_index[s[i]] = i
                if len(last_appear_index.keys()) == 26:
                    break
        
        left = 0
        while left < n:
            right = last_appear_index[s[left]]
            idx = left
            while idx < right:
                right = max(right, last_appear_index[s[idx]])
                idx += 1

            res.append(right - left + 1)
            left = right + 1

        return res

if __name__ == "__main__":
    input = "ababcbacadefegdehijhklij"

    s = Solution()
    print(s.partitionLabels(input))
