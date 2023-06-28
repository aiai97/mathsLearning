# hash_map = {}
# hash_map = {1:2,5:3,7:2}
# 1 in hash_map
# 9 in hash_map
# hash_map[5]
# hash_map[5] = 6
# hash_map[9] = 15
# del hash_map[9]
# len(hash_map)
# keys = hash_map.keys()
# for key in keys:
#     print(key)
#
# values = hash_map.values()
# for value in values:
#     print(value)
import unittest
from random import randint


# Example 1: 1. Two Sum

# Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target.
# You cannot use the same index twice.
# class Solution:
#     def twoSum(self,nums:list[int],target:int)->list[int]:
#         dict = {}
#         for i in range(len(nums)):
#             num = nums[i]
#             complement = target - num
#             if complement in dict:
#                 return [i,dict[complement]]
#             dict[num] = i
#         return [-1,-1]
# test_cases = [
#     ([2, 7, 11, 15], 9),  # Expected output: [0, 1]
#     ([3, 2, 4], 6),  # Expected output: [1, 2]
#     ([3, 3], 6),  # Expected output: [0, 1]
#     ([-1, 0, 1, 2, -1, -4], 0),  # Expected output: [1, 3]
#     ([], 10),  # Expected output: [-1, -1]
# ]
#
# for nums, target in test_cases:
#     result = Solution().twoSum(nums, target)
#     print(f"Input: nums = {nums}, target = {target}")
#     print("Output:", result)
#     print()

# Example 2: 2351. First Letter to Appear Twice

# Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.
# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         seen = set()
#         for c in s:
#             if c in seen:
#                 return c
#             seen.add(c)
#         return " "


# 测试数据 1
# s = "abcdeff"
# 重复字符为 "f"
# 预期输出: "f"

# 测试数据 2
# s = "abcdefg"
# 没有重复字符
# 预期输出: " "
# 实例化 Solution 类的对象
# solution = Solution()
# # 调用 repeatedCharacter 方法，并传入字符串作为参数
# result = solution.repeatedCharacter("abcdeff")
#
# # 打印结果
# print(result)

# Example 3: Given an integer array nums, find all the numbers x that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
# def find_numbers(nums):
#     ans = []
#     nums = set(nums)
#     for num in nums:
#         if (num+1 not in nums) and (num-1 in nums):
#             ans.append(num)
#     return ans
# class FindNumbersTestCase(unittest.TestCase):
#     def test_find_numbers(self):
#         nums = [1, 2, 3, 5, 6, 8, 9]
#         expected_result = [3,6,9]
#         result = find_numbers(nums)
#         self.assertEqual(result, expected_result)
#
#
# if __name__ == '__main__':
#     unittest.main()
# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_set = set()
        for char in sentence:
            alphabet_set.add(char)
        return len(alphabet_set) == 26


print(Solution.checkIfPangram(Solution, "thequickbrownfoxjumpsoverthelazydog"))  # True
print(Solution.checkIfPangram(Solution, "hello"))  # False
