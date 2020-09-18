#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] kth-largest-element-in-an-array
#
# 代码1：暴力排序
# Time: O(nlogn)
# Space: O(1)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse=True)
#                 return nums[k-1]


# 代码2：快排思想选择第k大元素
# Time: O(n)，极端情况下退化到O(n^2)
# Space: O(1)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         size = len(nums)  
#         target = size - k
#         left = 0
#         right = size - 1
#         while True:
#             index = self.partition(nums, left, right)
#             if index == target:
#                 return nums[target]
#             elif index < target:
#                 left = index + 1
#             else:
#                 right = index - 1

#     def partition(self, nums, left, right):
#         pivot = nums[left]
#         j = left
#         for i in range(left+1, right+1):
#             if nums[i] < pivot:
#                 j += 1
#                 nums[i], nums[j] = nums[j], nums[i]
#         nums[left], nums[j] = nums[j], nums[left]
#         return j


# 代码3：加入随机选择元素的快排方法
# Time: O(n)，随机选择避免极端情况
# Space: O(1)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         size = len(nums)  
#         target = size - k
#         left = 0
#         right = size - 1
#         while True:
#             index = self.partition(nums, left, right)
#             if index == target:
#                 return nums[target]
#             elif index < target:
#                 left = index + 1
#             else:
#                 right = index - 1
        
#     def partition(self, nums, left, right):
#         random_idx = random.randint(left, right)
#         nums[random_idx], nums[left] = nums[left], nums[random_idx]
        
#         pivot = nums[left]
#         j = left
#         for i in range(left+1, right+1):
#             if nums[i] < pivot:
#                 j += 1
#                 nums[i], nums[j] = nums[j], nums[i]
#         nums[left], nums[j] = nums[j], nums[left]
#         return j


# 代码4：Python内置堆方法，建立小根堆
# heapq.heapreplace(heap, item)弹出并返回heap中最小的一项，同时推入新的item
# Time:O(n + klgn)
# Space: O(k)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = nums[:k]
#         heapq.heapify(heap)
#         for num in nums[k:]:
#             if num > heap[0]:
#                 heapq.heapreplace(heap, num)
#         return heap[0]


# 代码5：同代码4，使用heappushpop
# heapq.heappushpop(heap, item)将item放入堆中，然后弹出并返回 heap 的最小元素
# heappushpop与heapreplace区别就是heappushpop弹出的元素不会比添加的元素大
# Time:O(n + klgn)
# Space: O(k)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = nums[:k]
#         heapq.heapify(heap)  # O(n)
#         for num in nums[k:]:
#             heapq.heappushpop(heap, num)  # O(klgn)
#         return heap[0]


# 代码6：Python内置堆方法，建立大根堆
# Time:O(n + klgn)
# PS：这里的时间复杂度其实按照大了说的
# 这种情况是Push和Pop分开的复杂度
# 内置函数可以将这两个函数放在一起来减少复杂度
# 如代码4、5的两个函数，和代码6的这个
# 真实时间复杂度其实更低，是O(k + (n-k) log k)
# 具体可参考维基百科或者堆的API：https://docs.python.org/zh-cn/3/library/heapq.html
# Space: O(k)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:  # Time: O(k + (n-k) log k), space: O(k)
#         ans = heapq.nlargest(k, nums) # run time O(n+klgn)
#         return ans[-1]


# 代码7：Python3大根堆的详细实现
# Time:O(n + klgn)
# Space: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:  # Time: O(k + (n-k) log k), space: O(k)
        def maxHeapify(nums, i):  # 递归不断修正大根堆
            largest = i           # 当前最大值索引默认为根节点索引i
            l = i * 2 + 1         # 左孩子索引
            r = i * 2 + 2         # 右孩子索引
            if l < len(nums) and nums[l] > nums[largest]:
                largest = l       # 如果左孩子值大于根节点，存储左孩子索引
            if r < len(nums) and nums[r] > nums[largest]:
                largest = r       # 如果右孩子值大于根节点，存储右孩子索引
            if largest != i:      # 递归终止条件，只在largest被左或右孩子更新的时候才递归
                nums[i], nums[largest] = nums[largest], nums[i]  # 左右孩子中大的值上浮
                maxHeapify(nums, largest)
        
        def buildMaxHeap(nums):                        # 将一个列表转为大根堆
            for i in range(len(nums) // 2 - 1, -1, -1):# 从最后一个非叶子节点开始向前遍历
                maxHeapify(nums, i)
                
        def findKthMax(nums, k):                       # 堆排序找到第k大元素
            buildMaxHeap(nums)                         # 建立大根堆
            for _ in range(k - 1):
                nums[0], nums[-1] = nums[-1], nums[0]  # 交换堆顶和堆尾元素，最大值沉底
                nums.pop()                             # O(1)时间删除最大值，防止最大值再次上浮
                maxHeapify(nums, 0)                    # 从堆顶修正大根堆
            return nums[0]
        
        return findKthMax(nums, k)
# @lc code=end