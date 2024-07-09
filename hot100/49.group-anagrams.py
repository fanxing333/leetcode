import collections


class Solution(object):
    def groupAnagrams_my(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 如何构造一个identifier？使字母异位词的id能相等？
        # 排除一个错误的identifier：set(str)，无法保证字母出现的次数是一样的
        hashtable = {}
        for s in strs:
            list_s = sorted(s)
            tuple_s = tuple(list_s)
            if tuple_s in hashtable:
                hashtable[tuple_s].append(s)
            else:
                hashtable[tuple_s] = [s]

        return list(hashtable.values())
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 如何构造一个identifier？使字母异位词的id能相等？
        # 排除一个错误的identifier：set(str)，无法保证字母出现的次数是一样的
        hashtable = collections.defaultdict(list)
        for s in strs:
            list_s = sorted(s)
            tuple_s = tuple(list_s)
            hashtable[tuple_s].append(s)

        return list(hashtable.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))