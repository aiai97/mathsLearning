# #Declaration: we will use deque from the collections module
# import collections
# queue = collections.deque()
#
# #If you want to initialize it with some initial values
# queue = collections.deque([1,2,3])
#
# # Enqueueing/adding elements
# queue.append(4)
# queue.append(5)
#
# # Dequeuing/removing elements:
# queue.popleft() # 1
# queue.popleft()  # 2
#
# # Check element at front of queue(next element to be removed)
# queue[0] # 3
#
# # Get size
# len(queue)
# from collections import deque
# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)
# while queue:
#     print(queue.popleft())
# Example: 933. Number of Recent Calls
#
# Implement the RecentCounter class. It should support ping(int t), which records a call at time t, and then returns an integer representing the number of calls that have happened in the range [t - 3000, t]. Calls to ping will have increasing t.
from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)
        return len(self.queue)
counter = RecentCounter()
# print(counter.ping(100))
# print(counter.ping(300))
# print(counter.ping(500))
# print(counter.ping(700))
# print(counter.ping(3500)) # Output: 4
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Implement the MovingAverage class:
#
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.


# class MovingAverage:
#     def __init__(self, size: int):
#         self.size = size
#         self.queue = []
#
#     def next(self, val: int) -> float:
#         if len(self.queue) < 10:
#             self.queue.append(val)
#             if len(self.queue) >= 4:
#                 ratio = round(sum(self.queue[1:4]) / sum(self.queue[0:3]),2)
#                 print(ratio)
#                 self.queue.pop()
#                 return ratio
# m = MovingAverage(4)
# m.next(1) # 输出 1.0
# m.next(2)  # 输出 1.5
# m.next(3)  # 输出 2.0
# # print(a)
# m.next(4)
# m.next(5)
# m.next(6)
class MovingAverage:
    def __init__(self,size:int):
        self.size = size
        self.queue = []
    def next(self,val:int) -> float:
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.queue.pop(0)
        return sum(self.queue) / len(self.queue)
# Example 1: 739. Daily Temperatures
#
# Given an array of integers temperatures that represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the
# i(index) day to get a warmer temperature. If there is no future day that is warmer, have answer[i] = 0 instead.
def dailyTemperatures(temperatures):
    n = len(temperatures)  # 输入数组的长度
    answer = [0] * n  #  初始化结果数组，初始值都为0
    stack = []  #  使用栈来存储未处理的日期
    for i in range(n):
        # 如果当前温度大于栈顶元素对应的温度
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index #计算等待天数
        stack.append(i)
    return answer


# class Solution5:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         answer = [0] * len(temperatures)
#
#         for i in range(len(temperatures)):
#             while stack and temperatures[stack[-1]] < temperatures[i]:
#                 j = stack.pop()
#                 answer[j] = i - j
#             stack.append(i)
#
#         return answer
# 评分数组：[80, 90, 75, 85, 95, 70]
# k = 3（需要选出前3名）
# descending sorted deque [80] [90] [90,75] [90,85] [95]       [95,70]
# ans                     []   []   [90]    [90,90] [90,90,95] [90,90,95,95]
# Example 2: 239. Sliding Window Maximum
#
# Given an integer array nums and an integer k, there is a sliding window of size k that moves from the very left to the very right. For each window, find the maximum element in the window.
#
# For example, given nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3, return [3, 3, 5, 5, 6, 7]. The first window is [1, 3, -1, -3, 5, 3, 6, 7] and the last window is [1, 3, -1, -3, 5, 3, 6, 7]
#
# Note: this problem is significantly more difficult than any problem we have looked at so far. Don't be discouraged if you are having trouble understanding the solution.

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        queue = deque()
        for i in range(len(nums)):
            # maintain monotonic decreasing.
            # all elements in the deque smaller than the current one
            # have no chance of being the maximum, so get rid of them
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element.
            # if queue[0] + k == i, then it is outside the window
            if queue[0] + k == i:
                queue.popleft()

            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans
