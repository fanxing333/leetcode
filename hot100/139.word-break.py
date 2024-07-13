from typing import List

class Solution:
    """
    如果一个字符串分割后，其所有子串都由 wordDict 组成，则返回 True
    isTrue(s[:j]) = isTrue(s[:i]) &  isTrue(s[i:j])
    or
    维护一个 is_true 数组
    is_true[i] 表示字符串 s[:i+1] 可以由 wordDict 组成
    is_true[i] = (is_true[0..i] and isTrue(s[0..i])) or :只要有一个为 True 即为 True

    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
            
        is_true = [False] * len(s)
        break_idx = []
        for i in range(len(s)):
            if s[:i+1] in wordDictSet:
                is_true[i] = True
                break_idx.append(i)
            
            else:
                # 如果 s[:i+1] 不在字典里，则查看 i+1 之前所有的分割点 break_idx
                # 如果 s[break_idx+1: i+1] 在字典里，则设为 1，否则设置为 0
                for idx in break_idx:
                    if s[idx + 1: i + 1] in wordDictSet:
                        is_true[i] = True
                        break_idx.append(i)
                        break
            print(break_idx)
        print(is_true)
        return is_true[-1]



if __name__ == "__main__":
    input = "leetcode"
    wordDict = ["lee", "code", "leet"]

    input = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

    s = Solution()
    print(s.wordBreak(input, wordDict))
