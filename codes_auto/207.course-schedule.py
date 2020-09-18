#
# @lc app=leetcode.cn id=207 lang=python
#
# [207] course-schedule
#
class Solution:
    def canFinish(self, numCourses, prerequisites):
        #用拓扑排序，来判断图是否是有环图
        #首先定义两个表，一个入度表，一个图的邻接表
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        #将题目给出的数据转换成入度表和邻接表
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        #然后开始用bfs进行，首先将入度为0的点入队
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        #开始迭代
        while queue:
            node = queue.pop(0)
            numCourses-=1                    #学完一门课
            for c in adjacency[node]:
                indegrees[c] -= 1            #节点入度减1
                if indegrees[c] == 0:        #入度变为0，意思已经学完了先修课程
                    queue.append(c)          #入队,循环
        
        return not numCourses                #判断课程是否都学完
# @lc code=end