
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

这道题目要求在给定的二进制数组中，最多可以将 k 个 0 翻转为 1，求得到的连续 1 的最长子数组的长度。

解题思路如下：

使用双指针法来解决这个问题。定义两个指针 left 和 right，分别表示子数组的左边界和右边界。

初始化 left 和 right 都为 0，表示子数组的范围是 [0, 0]。

当 right 指针遍历数组时，遇到 0 时，将 k 的值减 1。如果 k 小于 0，说明无法再翻转 0 了，此时需要将 left 指针右移直到遇到 0，同时将 k 的值加 1。

每次遍历都更新最长子数组的长度，即 right - left + 1。

遍历结束后，最长子数组的长度即为所求。

def longestOnes(nums, k):
    left = right = 0
    max_length = 0
    zero_count = 0

    while right < len(nums):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length
