from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        
        number_set = set([str(i) for i in range(10)])
        n = len(s)
        res = ""
        
        # 接收一个 idx，返回一个 str
        def build_str(idx):
            # s[idx] 一定是一个数字
            left, right = idx, idx + 1
            while s[right] != "[":
                right += 1
            repeat_time = int(s[left: right])

            left = right + 1
            right = right + 1
            total_str = ""
            while s[right] != "]":
                if s[right] in number_set:
                    sub_str, right = build_str(right)
                    total_str += sub_str
                else:
                    total_str += s[right]
                    right += 1
            
            return total_str * repeat_time, right + 1
        

        idx = 0
        
        while idx < n:
            if s[idx] in number_set:
                sub_str, idx = build_str(idx)
                res += sub_str
            else:
                res += s[idx]
                idx += 1

        return res



if __name__ == "__main__":
    input = "3[a]2[bc]"
    # input = "3[a2[c]]"

    s = Solution()
    print(s.decodeString(input))
