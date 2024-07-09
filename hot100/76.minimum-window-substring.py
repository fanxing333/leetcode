from typing import List

class Solution:
    """
    
    """
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
            
        min_window = ""
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1
        char_count_min = char_count.copy()
        
        for right in range(len(s)):
            if s[right] in char_count.keys():
                char_count[s[right]] += 1

            if all([count>=0 for count in char_count.values()]):
                # 找到了覆盖串，退出循环前将 left 移动到最大位置，形成一个最小覆盖串
                for left in range(right):
                    if s[left] in char_count.keys():
                        if char_count[s[left]] == 0:
                            break
                        else:
                            char_count[s[left]] -= 1

                min_window = s[left: right+1]
                break
        
        if right == len(s) - 1:
            return min_window
        
        # 程序运行到此时，必有 s[left: right+1] 覆盖住 t
        for right in range(right+1, len(s)):
            left += 1

            if s[left-1] in char_count.keys():
                if char_count[s[left-1]] > char_count_min[s[left-1]]:
                    char_count[s[left-1]] -= 1

            if s[right] in char_count.keys():
                char_count[s[right]] += 1

            if all([count>=0 for count in char_count.values()]):
                for left in range(left, right):
                    min_window = s[left: right+1]
                    if s[left] in char_count.keys():
                        if char_count[s[left]] == 0:
                            break
                        else:
                            char_count[s[left]] = max(char_count[s[left]] - 1, char_count_min[s[left]] )

        return min_window

    """
    第一个通过的版本
    还可以优化吗？
    left 右移时，每次都要判断一遍是否满足，有点冗余
    """
    def minWindow2(self, s: str, t: str) -> str:
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
            
        min_window = ""
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1
        char_count_min = char_count.copy()
        
        for right in range(len(s)):
            if s[right] in char_count.keys():
                char_count[s[right]] += 1

            if all([count>=0 for count in char_count.values()]):
                # 找到了覆盖串，退出循环前将 left 移动到最大位置，形成一个最小覆盖串
                for left in range(right):
                    if s[left] in char_count.keys():
                        if char_count[s[left]] == 0:
                            break
                        else:
                            char_count[s[left]] -= 1

                min_window = s[left: right+1]
                break
        
        if right == len(s) - 1:
            return min_window
        
        # 程序运行到此时，必有 s[left: right+1] 覆盖住 t
        for right in range(right+1, len(s)):
            left += 1

            if s[left-1] in char_count.keys():
                if char_count[s[left-1]] > char_count_min[s[left-1]]:
                    char_count[s[left-1]] -= 1

            if s[right] in char_count.keys():
                char_count[s[right]] += 1

            tag = False
            while all([count>=0 for count in char_count.values()]):
                tag = True
                min_window = s[left: right+1]
                left += 1
                if s[left-1] in char_count.keys():
                    if char_count[s[left-1]] > char_count_min[s[left-1]]:
                        char_count[s[left-1]] -= 1

            if tag:
                left -= 1
                char_count[s[left]] += 1

            
        return min_window



    """
    First thought:
    初始化阶段
        维护一个滑动窗口
        遍历 s，直到滑动窗口覆盖住 t，且滑动窗口的两端是 t 中的 char

    持续滑动阶段
        将滑动窗口不停向右移动，直到滑动窗口重新覆盖住 t，这时候滑动窗口的左界向右缩减直到最小覆盖
        重复上一步直到滑到底

    关键点
        维护一张表，统计滑动窗口内关键 char 的数量，这样每次滑动后都能知道滑动窗口是否仍然能覆盖住 t
    """
    def minWindow2(self, s: str, t: str) -> str:
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
            
        min_window = ""
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1
        
        char_count_min = char_count.copy()
        
        left = 0
        while s[left] not in char_count.keys():
            left += 1
            if left > len(s) - len(t):
                return min_window
            
        char_count[s[left]] += 1
        
        right = left + 1
        if left == len(s) - 1:
            return min_window
        
        while any([count<0 for count in char_count.values()]):
            if s[right] in char_count.keys():
                char_count[s[right]] += 1

            right += 1
            if right > len(s) - 1:
                if any([count<0 for count in char_count.values()]):
                    return min_window
                else:
                    tag = False
                    while all([count>=0 for count in char_count.values()]):
                        tag = True
                        left += 1
                        if s[left-1] in char_count.keys():
                            if char_count[s[left-1]] > char_count_min[s[left-1]]:
                                char_count[s[left-1]] -= 1

                    if tag:
                        left -= 1

                    return s[left: right]
            
        min_window = s[left: right]

        right -= 1
        while right < len(s):
            """"""
            # 窗口移动之后仍然能覆盖，窗口左界向右边缩减
            print(right, char_count)
            tag = False
            while all([count>=0 for count in char_count.values()]):
                tag = True
                min_window = s[left: right+1]
                left += 1
                if s[left-1] in char_count.keys():
                    if char_count[s[left-1]] > char_count_min[s[left-1]]:
                        char_count[s[left-1]] -= 1

            if tag:
                left -= 1

            """"""
            left += 1
            right += 1

            if s[left-1] in char_count.keys():
                if char_count[s[left-1]] > char_count_min[s[left-1]]:
                    char_count[s[left-1]] -= 1

            if right < len(s) and s[right] in char_count.keys():
                char_count[s[right]] += 1
            
        return min_window
        

if __name__ == "__main__":
    input = "ADOBECODEBANC"
    t = "ABC"

    input = "acbbaca"
    t = "aba"

    s = Solution()
    print(s.minWindow(input, t))
