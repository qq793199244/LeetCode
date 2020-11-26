'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
返回一个表示每个字符串片段的长度的列表。
示例：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
'''
class Solution(object):
    # 贪心算法+双指针
    def partitionLabels(self, S):
        n = len(S)
        if n == 0:
            return ''
        res = []
        # 存储每个字母最后一次出现的下标
        d = {}
        for i in range(n):
            d[S[i]] = i
        start = end = 0
        # 遍历整个字符串S
        for i in range(n):
            end = max(d[S[i]], end)
            if i == end:
                res.append(end-start+1)
                start = end + 1
        return res

if __name__ == '__main__':
    u = Solution()
    s = "ababcbacadefegdehijhklij"
    print(u.partitionLabels(s))