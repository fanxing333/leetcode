from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        if len(p) == 1:
            for idx in range(len(s)):
                if s[idx] == p:
                    res.append(idx)
            return res

        # 初始化 p_dict
        p_dict = {}
        for char in p:
            p_dict[char] = p_dict.get(char, 0) + 1
        
        # 找到满足要求的 left
        left = 0
        while left < len(s) and s[left] not in p_dict.keys():
            left += 1
        if left > len(s) - len(p):
            return res
        if p_dict[s[left]] == 1:
            del p_dict[s[left]] 
        else:
            p_dict[s[left]] -= 1

        right = left + 1
        # right 开始滑动
        while right < len(s):
            # 在 while 循环中，确保 s[left: right] 内的所有 char 都占 p 的一个位子，以便 reset p_dict
            if s[right] in p_dict.keys():
                if p_dict[s[right]] == 1:
                    del p_dict[s[right]] 
                else:
                    p_dict[s[right]] -= 1

                if len(p_dict) == 0:
                    res.append(left)
                    p_dict[s[left]] = p_dict.get(s[left], 0) + 1
                    left += 1
                    right += 1
                    continue
                else:
                    right += 1
                    continue
            else:
                # 如果 s[right] 不在 dict 中，那么可以重置滑动窗口
                # a. 即重新找到一个合法的 left，以及 right = left + 1
                # b. 在这之前需要 reset p_dict，即将 left 滑动到 right 之前
                # b
                if s[right] in set(p):
                    while s[left] != s[right]:
                        p_dict[s[left]] = p_dict.get(s[left], 0) + 1
                        left += 1

                    left += 1
                    right += 1
                    continue

                else:
                    while left < right:
                        p_dict[s[left]] = p_dict.get(s[left], 0) + 1
                        left += 1
                # a
                left = right + 1
                while left < len(s) and s[left] not in p_dict.keys():
                    left += 1
                if left > len(s) - len(p):
                    return res
                if p_dict[s[left]] == 1:
                    del p_dict[s[left]] 
                else:
                    p_dict[s[left]] -= 1
                
                right = left + 1

        return res



    def findAnagrams2(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        
        p_set = set(p)
        while left < len(s) - len(p) + 1 and s[left] not in p_set:
            left += 1
        if left > len(s) - len(p):
            return res
        tmp_set = set(p)
        tmp_set.remove(s[left])
        right = left + 1

        while right < len(s):
            if s[right] in tmp_set:
                tmp_set.remove(s[right])
                if len(tmp_set) == 0:
                    res.append(left)
                    tmp_set.add(s[left])
                    left += 1
                right += 1

            else:
                if s[right] in p_set:
                    while s[left] != s[right]:
                        tmp_set.add(s[left])
                        left += 1
                    left += 1
                    right += 1
                    continue
                else:
                    left = right + 1
                while left < len(s) - len(p) + 1 and s[left] not in p_set:
                    left += 1
                if left > len(s) - len(p):
                    return res
                tmp_set = set(p)
                tmp_set.remove(s[left])
                right = left + 1

        return res

if __name__ == "__main__":
    input = "cbaebabacd"
    p = "abc"

    s = Solution()
    print(s.findAnagrams(input, p))
