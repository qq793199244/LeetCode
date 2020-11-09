'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not str:
            return []
        # 当且仅当它们的排序字符串相等时，两个字符串是字母异位词。
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())


if __name__ == '__main__':
    u = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = u.groupAnagrams(strs)
    print(res)