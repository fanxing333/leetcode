from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort(reverse=True)

        def backtrace(first=0, target=target, output=[]):
            if first == n:
                return
            
            for i in range(first, n):
                if target - candidates[i] == 0:
                    res.append(output + [candidates[i]])
                elif target - candidates[i] > 0:
                    backtrace(i, target - candidates[i], output + [candidates[i]])

        backtrace()

        return res
    
    """
    hashtable[value] = [[combination]..]
    """
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        hashtable = {}

        for num in candidates:
            for key in list(hashtable.keys()):
                i = 1
                while key - i * num >= 0:
                    if key - i * num ==0:
                        # print(key, i, num)
                        res += [combination + [num] * i for combination in hashtable[i * num]]
                    else:
                        hashtable[key - i * num] = hashtable.get(key - i * num, []) + [combination + [num] * i for combination in hashtable[key]]

                    i += 1

            i = 1
            while target - i * num >= 0:
                if target - i * num == 0:
                    res.append(i * [num])
                # if i * num in hashtable.keys():
                #     res += [combination + [num] * i for combination in hashtable[i * num]]
                else:
                    hashtable[target - i * num] = hashtable.get(target - i * num, []) + [[num] * i]

                i+= 1

            print(hashtable)

        return res

if __name__ == "__main__":
    input = [2,3,5]
    target = 8

    s = Solution()
    print(s.combinationSum(input, target))
