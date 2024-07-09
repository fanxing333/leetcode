from typing import List

class Solution:
    """
    该方法是理想的滑动窗口，不需要维护任何其他变量，只在原数组 s 上进行操作，所以最终消耗内存分布击败了 99.55%

    执行用时击败了 94.82%，不确定 `s[right] in s[left: right]` 这个操作的复杂度，如果用 hash表 判断，会不会更快？但代价是要维护一个 hash 表
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_length = 1
        left = 0
        for right in range(1, len(s)):
            if s[right] in s[left: right]:
                while s[left] != s[right]:
                    left += 1
                left += 1
            
            max_length = max(max_length, right + 1 - left)

        return max_length
    
    """
    该方法维护了两个 hash 表，便于根据索引查找替换和删除
    """
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_length = 1
        char2idx = {s[0]: 0}
        idx2char = {0: s[0]}

        left, right = 0, 0
        while right < len(s) - 1:
            if s[right+1] in char2idx.keys():
                for del_idx in range(left, char2idx[s[right+1]] + 1):
                    del_char = idx2char[del_idx]
                    del idx2char[del_idx]
                    del char2idx[del_char]
                left = del_idx + 1
            
            char2idx[s[right+1]] = right+1
            idx2char[right+1] = s[right+1]

            right += 1
            max_length = max(max_length, right + 1 - left)

        return max_length
    

    def lengthOfLongestSubstring3(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_length = 1
        left, right = 0, 0
        while right < len(s) - 1:
            try:
                left = left + s[left: right+1].index(s[right+1]) + 1
            except ValueError:
                pass
            finally:
                right += 1
                max_length = max(max_length, right + 1 - left)

        
        return max_length

if __name__ == "__main__":
    input = "abcabcbb"
    s = Solution()
    print(s.lengthOfLongestSubstring(input))
