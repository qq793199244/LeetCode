'''
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，
我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
示例 1:
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；
并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        for cur in range(len(indegrees)):
            if not indegrees[cur]: queue.append(cur)
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        if numCourses:
            return False
        else:
            return True


if __name__ == '__main__':
    u = Solution()
    numCourses1 = 2
    numCourses2 = 2
    prerequisites1 = [[1,0]]
    prerequisites2 = [[1,0],[0,1]]
    print(u.canFinish(numCourses1, prerequisites1))
    print(u.canFinish(numCourses2, prerequisites2))
