'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[[7],
[2,2,3]]
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        n = len(candidates)
        res = []

        def dfs(i, tmp_sum, tmp_res):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp_res)
                return
            dfs(i, tmp_sum + candidates[i], tmp_res + [candidates[i]])
            dfs(i + 1, tmp_sum, tmp_res)

        dfs(0, 0, [])
        return res


if __name__ == '__main__':
    u = Solution()
    candidates1 = [2,3,6,7]
    target1 = 7
    candidates2 = [2,3,5]
    target2 = 8
    print(u.combinationSum(candidates1, target1))
    print(u.combinationSum(candidates2, target2))