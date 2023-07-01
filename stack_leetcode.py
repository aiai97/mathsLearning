# # Declaration: we will just use a list
# stack = []
#
# # Pushing elements
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# # Popping elements
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
#
# stack.append(5)
#
# # Check if empty
# not stack
#
# # Check element at top
# stack[-1]
#
# # Get size
# len(stack)
#
# if not stack:
#     print("Stack is empty!")
# else:
#     print(f"Stack is not empty,top is {stack[-1]}")
# Example 1: 20. Valid Parentheses
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, and each closing bracket closes exactly one open bracket.
#
# For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.
class Solution:
    def isValid(self,s:str) -> bool:
        stack = []
        matching = {"(":")","[": "]", "{": "}"}
        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False
                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False
        return not stack

# Example 2: 1047. Remove All Adjacent Duplicates In String
#
# You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.
#
# For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca". This is the final answer.
class Solution1:
    def remove_duplicate_strings(self,s:str)-> str:
        stack = []
        for c in s:
            if stack and stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
# Example 3: 844. Backspace String Compare
#
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
#
# For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".
class Solution2:
    def backspaceCompare(self,s:str,t:str)-> bool:
        def build(str):
            stack = []
            for c in str:
                if c !="#":
                    stack.append(c)
                else:
                    stack.pop()
            return "".join(stack)
        return build(s)==build(t)
# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
#
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
#
# The canonical path should have the following format:
#
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.
# 使用 '/' 分隔符将输入路径拆分成各个组件：['', 'home', '', 'user', '..', '.', 'documents', '']
# 初始化一个空栈：stack = []
# 遍历路径中的每个组件：
# 组件为空或为单个句点 '.'：忽略它。
# 组件为双句点 '..'：如果栈不为空，弹出栈顶元素，表示返回上一级目录。
# 其他情况：将组件压入栈中。
# 处理完所有组件后，使用 '/' 分隔符将栈中的元素连接起来，构造简化后的路径。
# 如果简化后的路径不为空，添加前导斜杠 '/'。
# 返回简化后的路径。
def simplifyPath(path:str):
    components = path.split("/")
    stack = []
    for c in components:
        if c == "" or c ==".":
            continue
        elif c == "..":
            if stack:
                stack.pop()
        else:
            stack.append(c)
    return "/"+"/".join(stack)
# path = "/home//user/.././documents/"
# simplified_path = simplifyPath(path)
# print(simplified_path)

# Given a string s of lower and upper case English letters.
#
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
#
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
#
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
#
# Notice that an empty string is also good.
# 这道题目要求我们将给定的字符串转换为"good string"，其中"good string"定义为不含有相邻的大小写字母对的字符串。我们可以通过移除使字符串变坏的相邻字符对来使字符串变好。
# #
# # 下面是一种可能的解决方案的思路：
# #
# # 初始化一个空栈，用于存储待检查的字符。
# # 遍历字符串s的每个字符：
# # 如果栈为空，将当前字符入栈。
# # 如果栈非空且当前字符与栈顶字符大小写相反，则将栈顶字符出栈，表示移除了一个相邻字符对。
# # 否则，将当前字符入栈。
# # 将栈中剩余的字符按照出栈顺序连接成字符串，即为最终的"good string"。
def makeGood(s:str):
    stack = []
    for char in s:
        if stack and abs(ord(char)-ord(stack[-1]))==32:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
s = "leEeetcode"
result = makeGood(s)
print(result)
