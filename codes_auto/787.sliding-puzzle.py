#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] sliding-puzzle
#
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited=set()
        neighbor=[[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        target=[1,2,3,4,5,0]
        source=[board[0]+board[1]]
        def findzero(lt):
            i=0
            while i<len(lt):
                if lt[i]==0:
                    break
                i+=1
            return i
        count=0
        while source:
            layer=[]
            for i in source:
                if i==target:
                    return count
                z=findzero(i)
                for j in neighbor[z]:
                    tmp=i[:]
                    tmp[z],tmp[j]=tmp[j],tmp[z]
                    if tuple(tmp) not in visited:
                        visited.add(tuple(tmp))
                        layer.append(tmp)
            source=layer
            count+=1
        return -1

# @lc code=end